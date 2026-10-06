#!/usr/bin/env python3
import re
import json
from pathlib import Path

from localization import encode_cpp, load_catalog, validate_translation
from update_feed import public_bytes


def plan_russian_titles(tdesktop, catalog=None, cmake_text=None):
    root = Path(tdesktop)
    source = root / 'Telegram/SourceFiles'
    catalog = catalog if catalog is not None else load_catalog(Path(__file__).resolve().parents[1] / 'i18n/ru.json')
    entry = catalog.get('title_template', {})
    if entry.get('source') != 'TELE #{build}':
        raise ValueError('Russian default title must bind to the upstream template')
    translated = entry.get('translation')
    validate_translation(entry['source'], translated)
    if re.findall(r'\{[^{}]*\}', translated) != ['{build}'] or translated.count('#{build}') != 1:
        raise ValueError('Russian default title must preserve #{build}')
    options = source / 'tele/tele_options.cpp'
    text = options.read_text(encoding='utf-8')
    default = '.defaultValue = u"TELE #{build}"_q,'
    include = '#include "tele/tele_title_template.h"'
    if text.count(default) != 1 or text.count(include) != 1:
        raise ValueError('Upstream default title changed; review localization')
    text = text.replace(default, '.defaultValue = ' + encode_cpp(translated, 'u') + '_q,')
    text = text.replace(include, include + '\n#include "tele/tele_russian_title.h"')
    for name in ('TitleTemplateOption', 'WindowTitleTemplateOption'):
        old = f'return {name}.value();'
        if text.count(old) != 2:
            raise ValueError('Upstream title getters changed; review localization')
        text = text.replace(old, f'return Tele::RussianDefaultTitle({name}.value());')
    header = source / 'tele/tele_russian_title.h'
    if header.exists():
        raise ValueError('Russian title helper already exists; prepare fresh source')
    legacy = ['TELE #{build}', 'TELE {build}', 'TELERU #{build}', translated]
    conditions = '\n\t\t|| '.join('source == ' + encode_cpp(value, 'u') + '_q' for value in legacy)
    helper = '#pragma once\n\n#include "tele/tele_lowercase.h"\n\nnamespace Tele {\n\ninline QString RussianDefaultTitle(const QString &source) {\n\treturn (' + conditions + ')\n\t\t? Lower(' + encode_cpp(translated, 'u') + '_q)\n\t\t: source;\n}\n\n}\n'
    cmake = root / 'Telegram/CMakeLists.txt'
    cmake_text = cmake_text if cmake_text is not None else cmake.read_text(encoding='utf-8')
    marker = '    tele/tele_options.h\n'
    if cmake_text.count(marker) != 1:
        raise ValueError('Upstream tele source list changed')
    return {options: text, header: helper, cmake: cmake_text.replace(marker, marker + '    tele/tele_russian_title.h\n')}


def plan_russian_plurals(tdesktop, catalog=None):
    root = Path(tdesktop)
    source = root / 'Telegram/SourceFiles'
    box = source / 'tele/tele_settings_io_box.cpp'
    text = box.read_text(encoding='utf-8')
    original = "[[nodiscard]] QString Plural(int count, const QString &one) {\n\treturn (count == 1) ? one : (one + 's');\n}"
    if text.count(original) != 1:
        raise ValueError('Upstream settings plural function changed; review Russian forms')
    nouns = re.findall(r'Plural\([^\n]*,\s*u"([^"\n]+)"_q\)', text)
    if not nouns or set(nouns) != {'setting'}:
        raise ValueError('Upstream settings plural nouns changed; review Russian forms')
    catalog = catalog if catalog is not None else load_catalog(Path(__file__).resolve().parents[1] / 'i18n/ru.json')
    forms = catalog.get('plurals', {}).get('setting')
    if not isinstance(forms, list) or len(forms) != 3:
        raise ValueError('Russian setting needs exactly three plural forms')
    for form in forms:
        validate_translation('setting', form)
    values = ',\n'.join('\t\tLower(' + encode_cpp(form, 'u') + '_q)' for form in forms)
    replacement = "[[nodiscard]] QString Plural(int count, const QString &one) {\n\t(void)one;\n\treturn QStringList{\n" + values + "\n\t}.at(Tele::RussianPluralIndex(count));\n}"
    include = '#include "tele/tele_lowercase.h"'
    if text.count(include) != 1:
        raise ValueError('Upstream settings includes changed')
    text = text.replace(include, include + '\n#include "tele/tele_russian_plural.h"').replace(original, replacement)
    header = source / 'tele/tele_russian_plural.h'
    if header.exists():
        raise ValueError('Russian plural helper already exists; prepare fresh source')
    cmake = root / 'Telegram/CMakeLists.txt'
    cmake_text = cmake.read_text(encoding='utf-8')
    marker = '    tele/tele_options.h\n'
    if cmake_text.count(marker) != 1:
        raise ValueError('Upstream tele source list changed')
    helper = '#pragma once\n\nnamespace Tele {\n\nconstexpr int RussianPluralIndex(int count) {\n\tconst auto last100 = (count < 0) ? -(count % 100) : (count % 100);\n\tconst auto last10 = last100 % 10;\n\treturn (last100 >= 11 && last100 <= 14) ? 2\n\t\t: (last10 == 1) ? 0\n\t\t: (last10 >= 2 && last10 <= 4) ? 1\n\t\t: 2;\n}\n\n}\n'
    return {box: text, header: helper, cmake: cmake_text.replace(marker, marker + '    tele/tele_russian_plural.h\n')}


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
    changes.update(plan_russian_plurals(tdesktop))
    cmake = Path(tdesktop) / 'Telegram/CMakeLists.txt'
    changes.update(plan_russian_titles(tdesktop, cmake_text=changes[cmake]))
    return changes


def apply_overlay(tdesktop, repository="Duerotator/teleru", key_path=None, changes=None):
    changes = changes if changes is not None else plan_overlay(tdesktop, repository, key_path)
    for path, content in changes.items():
        reference = path if path.exists() else Path(tdesktop) / 'Telegram/SourceFiles/tele/tele_options.cpp'
        newline = "\r\n" if b"\r\n" in reference.read_bytes() else "\n"
        path.write_bytes(content.replace("\r\n", "\n").replace("\n", newline).encode("utf-8"))
    return list(changes)
