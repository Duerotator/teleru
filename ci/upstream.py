#!/usr/bin/env python3
import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCK = ROOT / "TELE_UPSTREAM.json"
REPOSITORY = "nitreojs/tele"
URL = f"https://github.com/{REPOSITORY}.git"


def git(path, *args):
    return subprocess.check_output(["git", "-C", str(path), *args], text=True, encoding="utf-8").strip()


def read_lock(path=LOCK):
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("repository") != REPOSITORY:
        raise ValueError("Unexpected upstream repository")
    if not re.fullmatch(r"v\d+\.\d+\.\d+-tele\.\d+", data.get("tag", "")):
        raise ValueError("Invalid tele release tag")
    if not re.fullmatch(r"[0-9a-f]{40}", data.get("commit", "")):
        raise ValueError("Pin the full 40-character upstream commit")
    if not re.fullmatch(r"v\d+\.\d+\.\d+", data.get("tdesktop", "")):
        raise ValueError("Invalid Telegram Desktop tag")
    return data


def checkout(data, path):
    path = Path(path).resolve()
    created = not path.exists()
    if created:
        path.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", "--no-checkout", "--filter=blob:none", URL, str(path)], check=True)
    if git(path, "remote", "get-url", "origin") != URL:
        raise ValueError(f"{path} belongs to another repository")
    head = subprocess.run(["git", "-C", str(path), "rev-parse", "--verify", "HEAD"], capture_output=True)
    if not created and head.returncode == 0 and git(path, "status", "--porcelain"):
        raise ValueError(f"Uncommitted changes in {path}")
    git(path, "fetch", "--depth=1", "origin", f"refs/tags/{data['tag']}")
    commit = git(path, "rev-parse", "FETCH_HEAD^{commit}")
    if commit != data["commit"]:
        raise ValueError(f"Upstream tag moved: expected {data['commit']}, got {commit}")
    git(path, "checkout", "--detach", commit)
    if (path / "UPSTREAM").read_text(encoding="utf-8").strip() != data["tdesktop"]:
        raise ValueError("The Telegram Desktop tag differs from the pinned tele release")
    return path


def api(endpoint):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "teleru-sync"}
    token = os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(f"https://api.github.com/repos/{REPOSITORY}/{endpoint}", headers=headers)
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def apply_queue(source, tdesktop):
    spec = importlib.util.spec_from_file_location("pinned_tele", source / "tele.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    environment = os.environ.copy()
    for variable, config, default in [("GIT_COMMITTER_NAME", "user.name", "teleru build"), ("GIT_COMMITTER_EMAIL", "user.email", "teleru-build@localhost")]:
        result = subprocess.run(["git", "-C", str(tdesktop), "config", "--get", config], capture_output=True, text=True)
        environment.setdefault(variable, result.stdout.strip() or default)

    def run_git(path, *args):
        if args and args[0] == "am" and any(str(a).endswith(".patch") for a in args):
            options = [str(a) for a in args if not str(a).endswith(".patch")]
            patches = [Path(a).read_bytes() for a in args if str(a).endswith(".patch")]
            result = subprocess.run(["git", *options], cwd=path, input=b"\n".join(patches), capture_output=True, env=environment)
            return subprocess.CompletedProcess(result.args, result.returncode, result.stdout.decode("utf-8", errors="replace"), result.stderr.decode("utf-8", errors="replace"))
        return subprocess.run(["git", *map(str, args)], cwd=path, capture_output=True, text=True, encoding="utf-8", errors="replace", env=environment)

    module.run_git = run_git
    try:
        module.cmd_apply(argparse.Namespace(tdesktop=tdesktop.resolve()))
    except module.Fail as error:
        raise ValueError(str(error)) from error


def latest():
    release = api("releases/latest")
    if release["draft"] or release["prerelease"]:
        raise ValueError("Expected a stable published release")
    tag = release["tag_name"]
    if not re.fullmatch(r"v\d+\.\d+\.\d+-tele\.\d+", tag):
        raise ValueError("Unexpected upstream release tag")
    obj = api(f"git/ref/tags/{tag}")["object"]
    for _ in range(5):
        if obj["type"] == "commit":
            break
        if obj["type"] != "tag":
            raise ValueError("Release tag does not point to a commit")
        obj = api(f"git/tags/{obj['sha']}")["object"]
    else:
        raise ValueError("Too many nested annotated tags")
    data = {"repository": REPOSITORY, "tag": tag, "commit": obj["sha"], "tdesktop": tag.split("-tele.")[0]}
    request = urllib.request.Request(f"https://raw.githubusercontent.com/{REPOSITORY}/{obj['sha']}/UPSTREAM")
    with urllib.request.urlopen(request, timeout=60) as response:
        actual = response.read().decode("utf-8").strip()
    if actual != data["tdesktop"]:
        raise ValueError("Release tag and UPSTREAM disagree")
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["version", "checkout", "apply", "update"])
    parser.add_argument("--destination", type=Path)
    parser.add_argument("--tdesktop", type=Path)
    parser.add_argument("--github-output", type=Path)
    args = parser.parse_args()
    data = read_lock()
    if args.command == "version":
        print(data["tdesktop"])
    elif args.command == "update":
        new = latest()
        changed = new != data
        if new["tag"] == data["tag"] and new["commit"] != data["commit"]:
            raise ValueError("Published upstream tag has been rewritten")
        if tuple(map(int, re.findall(r'\d+', new['tag']))) < tuple(map(int, re.findall(r'\d+', data['tag']))):
            raise ValueError('Refusing to downgrade the pinned upstream release')
        if changed:
            LOCK.write_text(json.dumps(new, indent=2) + "\n", encoding="utf-8")
        if args.github_output:
            with args.github_output.open("a", encoding="utf-8") as output:
                output.write(f"changed={str(changed).lower()}\ntag={new['tag']}\n")
        print(f"{'Updated' if changed else 'Already tracking'} {new['tag']} ({new['commit']})")
    else:
        if args.command == "apply" and not args.tdesktop:
            parser.error("apply requires --tdesktop")
        destination = args.destination or (args.tdesktop.resolve().parent / "tele-upstream" if args.tdesktop else ROOT / ".tele-upstream")
        source = checkout(data, destination)
        if args.command == "apply":
            if git(args.tdesktop, 'status', '--porcelain'):
                raise ValueError('The Telegram Desktop checkout has uncommitted changes')
            current = git(args.tdesktop, "describe", "--tags", "--exact-match", "HEAD")
            if current != data["tdesktop"]:
                raise ValueError("Apply the queue to a clean checkout of the pinned Telegram Desktop tag")
            apply_queue(source, args.tdesktop)
        print(f"Pinned tele sources: {source}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"Upstream preparation failed: {error}", file=sys.stderr)
        sys.exit(1)
