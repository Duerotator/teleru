#!/usr/bin/env python3
import argparse
import base64
import hashlib
import json
import os
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC_KEY = ROOT / "ci/update-public-key.pem"
PLATFORMS = {"win64": "tele.exe", "linux64": "tele", "macos": "tele.app/Contents/MacOS/tele"}


def public_bytes(path=PUBLIC_KEY):
    text = path.read_text(encoding="ascii")
    der = base64.b64decode("".join(line for line in text.splitlines() if not line.startswith("---")), validate=True)
    if len(der) != 44 or der[:12] != bytes.fromhex("302a300506032b6570032100"):
        raise ValueError("Expected an Ed25519 public key")
    return der[12:]


def generate(private_path, public_path=PUBLIC_KEY):
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    if private_path.exists():
        raise ValueError("Private key already exists; do not rotate an installed client's key accidentally")
    key = Ed25519PrivateKey.generate()
    private_path.parent.mkdir(parents=True, exist_ok=True)
    with private_path.open("xb") as output:
        output.write(key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()))
    if os.name != "nt":
        private_path.chmod(0o600)
    public_path.write_bytes(key.public_key().public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo))
    print(f"Private key saved to {private_path}; public key saved to {public_path}. Private key was not printed.")


def sign_feed(feed, private_pem, public_path=PUBLIC_KEY):
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    private = serialization.load_pem_private_key(private_pem.encode("ascii"), password=None)
    if not isinstance(private, Ed25519PrivateKey):
        raise ValueError("TELE_UPDATE_KEY must contain an Ed25519 private key")
    expected = public_bytes(public_path)
    actual = private.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
    if actual != expected:
        raise ValueError("TELE_UPDATE_KEY does not match the public key embedded in teleru")
    data = json.dumps(feed, ensure_ascii=True, separators=(",", ":")).encode("ascii")
    signature = private.sign(data)
    private.public_key().verify(signature, data)
    return {"feed": base64.b64encode(data).decode("ascii"), "signature": base64.b64encode(signature).decode("ascii")}


def create_feeds(directory, tag, base, counter, repository, private_pem, platforms, legacy_bootstrap=False):
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", repository) or repository == "nitreojs/tele":
        raise ValueError("Publish updates in the teleru repository")
    if not re.fullmatch(r"v\d+\.\d+\.\d+-tele\.\d+", tag) or base <= 0 or counter <= 0:
        raise ValueError("Invalid update version")
    if int(tag.rsplit('.', 1)[1]) != counter:
        raise ValueError('The release tag and update counter disagree')
    if not platforms or len(set(platforms)) != len(platforms) or any(p not in PLATFORMS for p in platforms):
        raise ValueError('Invalid platform list')
    sign_feed({}, private_pem)
    outputs = []
    for platform in platforms:
        archive = directory / f"tele-{tag}-{platform}.zip"
        with zipfile.ZipFile(archive) as file:
            entry = file.getinfo(PLATFORMS[platform])
            digest = hashlib.sha256()
            with file.open(entry) as binary:
                for chunk in iter(lambda: binary.read(1024 * 1024), b""):
                    digest.update(chunk)
        zip_digest = hashlib.sha256()
        with archive.open("rb") as binary:
            for chunk in iter(lambda: binary.read(1024 * 1024), b""):
                zip_digest.update(chunk)
        feed = {"tag": tag, "base": base, "counter": counter, "url": f"https://github.com/{repository}/releases/download/{tag}/{archive.name}", "zip_sha256": zip_digest.hexdigest(), "exe_sha256": digest.hexdigest()}
        envelope = sign_feed(feed, private_pem)
        target = directory / f"teleru-update-{platform}.json"
        target.write_text(json.dumps(envelope) + "\n", encoding="ascii")
        outputs.append(target)
        if legacy_bootstrap:
            target = directory / f"tele-update-{platform}.json"
            target.write_text(json.dumps(envelope | {"signature": ""}) + "\n", encoding="ascii")
            outputs.append(target)
    return outputs


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    key = sub.add_parser("generate-key")
    key.add_argument("--private-key", type=Path, default=ROOT / ".local/update-private-key.pem")
    sub.add_parser("check-key")
    feed = sub.add_parser("sign")
    feed.add_argument("--directory", type=Path, default=Path.cwd())
    feed.add_argument("--tag", required=True)
    feed.add_argument("--base", required=True, type=int)
    feed.add_argument("--counter", required=True, type=int)
    feed.add_argument("--repository", required=True)
    feed.add_argument("--platforms", nargs="+", choices=PLATFORMS, required=True)
    feed.add_argument("--legacy-bootstrap", action="store_true")
    args = parser.parse_args()
    if args.command == "generate-key":
        generate(args.private_key)
        return
    private_pem = os.environ.get("TELE_UPDATE_KEY", "")
    if not private_pem:
        raise ValueError("Set TELE_UPDATE_KEY to the private Ed25519 PEM")
    if args.command == "check-key":
        sign_feed({}, private_pem)
        print("Update signing key matches the client's public key")
    else:
        for path in create_feeds(args.directory, args.tag, args.base, args.counter, args.repository, private_pem, args.platforms, args.legacy_bootstrap):
            print(path.name)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, zipfile.BadZipFile) as error:
        print(f"Update feed failed: {error}", file=sys.stderr)
        sys.exit(1)
