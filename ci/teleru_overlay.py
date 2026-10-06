#!/usr/bin/env python3
import re
import json
from pathlib import Path

from update_feed import public_bytes


def replace_constant(text, name, value):
    pattern = rf'(constexpr\s+auto\s+{re.escape(name)}\s*=\s*)"(?:\\.|[^"\\])*"(?:\s*"(?:\\.|[^"\\])*")*\s*;'
    updated, count = re.subn(pattern, lambda m: m.group(1) + f'"{value}";', text)
    if count != 1:
        raise ValueError(f"Upstream changed {name}; expected one definition, found {count}")
    return updated


def plan_overlay(tdesktop, repository="Duerotator/teleru", key_path=None):
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", repository) or repository == "nitreojs/tele":
        raise ValueError("Invalid teleru update repository")
    source = Path(tdesktop) / "Telegram/SourceFiles"
    updater = source / "tele/tele_updater.cpp"
    text = updater.read_text(encoding="utf-8")
    guard = "if (!Core::Updates::VerifySignature(key, feed, signature, &error)) {"
    if text.count(guard) != 1:
        raise ValueError("Upstream signature verification changed; refusing an unsigned updater")
    text = replace_constant(text, "kFeedUrlPrefix", f"https://github.com/{repository}/releases/latest/download/teleru-update-")
    text = replace_constant(text, "kDownloadPrefix", f"https://github.com/{repository}/releases/download/")
    key = public_bytes(key_path) if key_path else public_bytes()
    text = replace_constant(text, "kPublicKeyHex", key.hex())
    changes = {updater: text}
    changelog = source / "tele/tele_changelog.cpp"
    changes[changelog] = replace_constant(changelog.read_text(encoding="utf-8"), "kReleasesPrefix", f"https://github.com/{repository}/releases/")
    changes[changelog] = replace_constant(changes[changelog], 'kReleasesUrl', f'https://github.com/{repository}/releases')
    history = source / 'tele/tele_changelog_history.cpp'
    content = history.read_text(encoding='utf-8')
    for name, value in {
        'kListUrl': f'https://api.github.com/repos/{repository}/releases?per_page=30',
        'kDownloadPrefix': f'https://github.com/{repository}/releases/download/',
        'kReleasesPrefix': f'https://github.com/{repository}/releases/',
        'kRepoPrefix': f'https://github.com/{repository}/',
    }.items():
        content = replace_constant(content, name, value)
    if content.count('tdata/tele_changelogs.json') != 1:
        raise ValueError('Upstream changelog cache path changed')
    changes[history] = content.replace('tdata/tele_changelogs.json', 'tdata/teleru_changelogs.json')
    bundled = Path(tdesktop) / 'Telegram/Resources/tele/changelog_history.json'
    if not bundled.exists():
        raise ValueError('Upstream bundled changelog path changed')
    first_tag = 'v7.2.9-tele.1'
    first_url = f'https://github.com/{repository}/releases/tag/{first_tag}'
    changes[bundled] = json.dumps({'releases': [{
        'version': 1, 'tag': first_tag, 'title': 'teleru 1', 'url': first_url,
        'items': [{'text': 'Первый выпуск русской версии teleru.', 'where': 'tele → Обновления',
            'category': 'Обновления', 'options': [], 'url': first_url}],
    }]}, ensure_ascii=False, indent=2) + '\n'
    prepare = Path(tdesktop) / "Telegram/build/prepare/prepare.py"
    if prepare.exists():
        changes[prepare] = prepare.read_text(encoding="utf-8").replace("mingw-w64-x86_64-diffutils", "diffutils")
    return changes


def apply_overlay(tdesktop, repository="Duerotator/teleru", key_path=None, changes=None):
    changes = changes if changes is not None else plan_overlay(tdesktop, repository, key_path)
    for path, content in changes.items():
        newline = "\r\n" if b"\r\n" in path.read_bytes() else "\n"
        path.write_bytes(content.replace("\r\n", "\n").replace("\n", newline).encode("utf-8"))
