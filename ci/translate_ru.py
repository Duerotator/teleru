#!/usr/bin/env python3
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

from localization import ROOT, run
from teleru_overlay import apply_overlay, plan_overlay


def fingerprint():
    paths = [ROOT / 'TELE_UPSTREAM.json', *sorted((ROOT / 'i18n').rglob('*.json')),
        *sorted((ROOT / 'ci').glob('*.py')), ROOT / 'ci/js_literals.cjs', ROOT / 'ci/update-public-key.pem', ROOT / 'ci/package-lock.json']
    digest = hashlib.sha256()
    for path in paths:
        digest.update(path.relative_to(ROOT).as_posix().encode())
        digest.update(path.read_bytes().replace(b'\r\n', b'\n'))
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tdesktop", type=Path)
    parser.add_argument("--report", type=Path, default=ROOT / "localization-report.json")
    parser.add_argument("--inventory", type=Path)
    args = parser.parse_args()
    tdesktop = args.tdesktop.resolve()
    location = subprocess.check_output(['git', '-C', str(tdesktop), 'rev-parse', '--git-path', 'teleru-localization.json'], text=True).strip()
    stamp = Path(location)
    if not stamp.is_absolute():
        stamp = tdesktop / stamp
    inputs = fingerprint()
    if stamp.exists():
        state = json.loads(stamp.read_text(encoding='utf-8'))
        if state.get('inputs') != inputs:
            raise ValueError('Localization inputs changed; prepare a fresh pinned source checkout')
        for relative, expected in state['files'].items():
            if hashlib.sha256((tdesktop / relative).read_bytes()).hexdigest() != expected:
                raise ValueError('Localized source changed; prepare a fresh source checkout')
        args.report.write_text(json.dumps(state['report'], ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        if args.inventory:
            args.inventory.write_text(json.dumps(state['inventory'], ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print('The exact Russian overlay is already applied and verified.')
        return 0
    plan_overlay(tdesktop)
    if not run(tdesktop, ROOT / "i18n/ru.json", args.report, args.inventory, apply_changes=True):
        return 1
    inventory = json.loads(args.inventory.read_text(encoding='utf-8')) if args.inventory else []
    apply_overlay(tdesktop)
    tracked = subprocess.check_output(['git', '-C', str(tdesktop), 'diff', '--name-only', '--diff-filter=AM'], text=True).splitlines()
    files = {p: hashlib.sha256((tdesktop / p).read_bytes()).hexdigest() for p in tracked}
    stamp.write_text(json.dumps({'inputs': inputs, 'files': files, 'report': json.loads(args.report.read_text(encoding='utf-8')), 'inventory': inventory}, ensure_ascii=False), encoding='utf-8')
    print("Russian catalog applied; updater and changelog point to teleru; signed updates required.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError) as error:
        print(f"teleru localization failed: {error}", file=sys.stderr)
        sys.exit(1)
