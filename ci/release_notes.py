#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--json", dest="json_path", type=Path, required=True)
    args = parser.parse_args()
    lock = json.loads((ROOT / "TELE_UPSTREAM.json").read_text(encoding="utf-8"))
    upstream_url = f"https://github.com/{lock['repository']}/releases/tag/{lock['tag']}"
    url = f"https://github.com/{args.repository}/releases/tag/{args.tag}"
    text = f"Русская сборка на основе {lock['tag']}. Перевод проверяется перед сборкой; обновления поступают из релизов teleru."
    args.out.write_text(f"# teleru {args.tag}\n\n{text}\n\nИсходный релиз: [{lock['tag']}]({upstream_url}).\n\nCommit исходников: `{lock['commit']}`.\n", encoding="utf-8")
    changelog = {"tag": args.tag, "title": f"teleru {args.tag}", "categories": ["Обновления"], "items": [{"text": text, "where": "tele → Обновления", "category": "Обновления", "url": url}], "url": url}
    args.json_path.write_text(json.dumps(changelog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
