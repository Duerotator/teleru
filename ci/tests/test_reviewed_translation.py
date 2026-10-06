import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from localization import ROOT, load_catalog, resolve, validate_translation
from teleru_overlay import apply_overlay, plan_russian_plurals, plan_russian_titles
import translate_ru


class ReviewedTranslationTests(unittest.TestCase):
    def fixture(self, root):
        source = root / 'Telegram/SourceFiles/tele'
        source.mkdir(parents=True)
        box = source / 'tele_settings_io_box.cpp'
        box.write_text('#include "tele/tele_lowercase.h"\n[[nodiscard]] QString Plural(int count, const QString &one) {\n\treturn (count == 1) ? one : (one + \'s\');\n}\nconst auto x = Plural(5, u"setting"_q);\n', encoding='utf-8')
        (source / 'tele_options.cpp').write_bytes(b'test\r\n')
        cmake = root / 'Telegram/CMakeLists.txt'
        cmake.write_text('nice_target_sources(Telegram ${src_loc}\nPRIVATE\n    tele/tele_options.h\n)\n')
        return box, cmake

    def test_reviewed_settings_keep_source_binding(self):
        catalog = load_catalog(ROOT / 'i18n/ru.json')
        entry = catalog['options']['kOptionChatListNoReorderAnimation']['name']
        record = dict(file='tele/tele_options.cpp', option='kOptionChatListNoReorderAnimation', field='name', source=entry['source'], display=True, technical=None)
        self.assertEqual(resolve(record, catalog), ('translated', 'Мгновенно перемещать чаты в списке'))
        self.assertEqual(resolve(record | {'source': entry['source'] + ' changed'}, catalog)[0], 'missing')

    def test_reviewed_settings_preserve_important_conditions(self):
        catalog = load_catalog(ROOT / 'i18n/ru.json')
        expected = {
            'kOptionKeepDeletedOwn': 'с этого устройства',
            'kOptionScreenshotSecretMedia': 'остаются защищёнными',
            'kOptionCalcmulaInline': 'Tab',
            'kOptionPunctualScheduled': 'приложение запущено',
            'kOptionViewAsTl': 'внешнем сайте schema.jppgr.am',
            'kOptionNftPurchasePrice': 'номеров',
            'kOptionMultiQuote': 'сообщение, на которое вы отвечаете',
        }
        for option, condition in expected.items():
            self.assertIn(condition, catalog['options'][option]['desc']['translation'], option)

    def test_sending_page_is_not_scheduled_messages(self):
        catalog = load_catalog(ROOT / 'i18n/ru.json')
        self.assertEqual(catalog['contexts']['settings/settings_tele.cpp']['Sending'], 'Отправка сообщений')
        self.assertEqual(catalog['strings']['Scheduled messages'], 'Отложенные сообщения')

    def title_fixture(self, root):
        _, cmake = self.fixture(root)
        options = root / 'Telegram/SourceFiles/tele/tele_options.cpp'
        options.write_text('#include "tele/tele_title_template.h"\n.defaultValue = u"TELE #{build}"_q,\nreturn TitleTemplateOption.value();\nreturn TitleTemplateOption.value();\nreturn WindowTitleTemplateOption.value();\nreturn WindowTitleTemplateOption.value();\n', encoding='utf-8')
        return options, cmake

    def test_standard_title_is_cyrillic_and_cmake_keeps_both_helpers(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            options, cmake = self.title_fixture(root)
            first = plan_russian_plurals(root)
            changes = plan_russian_titles(root, cmake_text=first[cmake])
            self.assertIn('.defaultValue = u"ТЕЛЕ #{build}"_q,', changes[options])
            self.assertEqual(changes[options].count('RussianDefaultTitle('), 4)
            self.assertIn('tele/tele_russian_plural.h', changes[cmake])
            self.assertIn('tele/tele_russian_title.h', changes[cmake])
            helper = changes[root / 'Telegram/SourceFiles/tele/tele_russian_title.h']
            self.assertIn('source == u"TELE #{build}"_q', helper)
            self.assertIn('Lower(u"ТЕЛЕ #{build}"_q)', helper)
            self.assertIn(': source;', helper)

    def test_changed_default_title_blocks(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            options, _ = self.title_fixture(root)
            options.write_text(options.read_text().replace('TELE #{build}', 'TELE {version}'))
            with self.assertRaises(ValueError):
                plan_russian_titles(root)

    def test_title_translation_keeps_build_variable(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.title_fixture(root)
            for translation in ['ТЕЛЕ', 'ТЕЛЕ {build}', 'ТЕЛЕ #{version}', 'ТЕЛЕ #{build} {name}', 'ТЕЛЕ #{build} #{build}']:
                with self.assertRaises(ValueError):
                    plan_russian_titles(root, {'title_template': {'source': 'TELE #{build}', 'translation': translation}})

    def test_workflows_only_start_by_request(self):
        for path in (ROOT / '.github/workflows').glob('*.yml'):
            text = path.read_text(encoding='utf-8')
            triggers = text.split('on:\n', 1)[1].split('\npermissions:', 1)[0]
            self.assertIn('  workflow_dispatch:', triggers, path.name)
            for trigger in ['schedule:', 'push:', 'workflow_run:', 'pull_request:', 'repository_dispatch:']:
                self.assertNotIn('  ' + trigger, triggers, path.name)

    def test_reviewed_placeholders_are_preserved(self):
        reviewed = json.loads((ROOT / 'i18n/ru/reviewed-settings.json').read_text(encoding='utf-8'))
        for option in reviewed['options'].values():
            for entry in option.values():
                validate_translation(entry['source'], entry['translation'])
        for source, translation in reviewed['strings'].items():
            validate_translation(source, translation)

    def test_plural_helper_is_in_tele_cmake_sources(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            box, cmake = self.fixture(root)
            changes = plan_russian_plurals(root)
            self.assertIn('Lower(u"настройка"_q)', changes[box])
            self.assertIn('Lower(u"настройки"_q)', changes[box])
            self.assertIn('Lower(u"настроек"_q)', changes[box])
            self.assertIn('tele/tele_russian_plural.h', changes[cmake])
            paths = apply_overlay(root, changes=changes)
            header = root / 'Telegram/SourceFiles/tele/tele_russian_plural.h'
            self.assertIn(header, paths)
            raw = header.read_bytes()
            self.assertIn(b'\r\n', raw)
            self.assertNotIn(b'\n', raw.replace(b'\r\n', b''))

    def test_changed_plural_source_blocks(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            box, _ = self.fixture(root)
            box.write_text(box.read_text().replace("one + 's'", "one + 'es'"))
            with self.assertRaises(ValueError):
                plan_russian_plurals(root)

    def test_new_plural_noun_blocks(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            box, _ = self.fixture(root)
            box.write_text(box.read_text().replace('u"setting"_q', 'u"chat"_q'))
            with self.assertRaises(ValueError):
                plan_russian_plurals(root)

    def test_missing_or_invalid_plural_forms_block(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture(root)
            for forms in [None, [], ['настройка'], ['настройка', '', 'настроек'], ['%1', 'настройки', 'настроек']]:
                with self.assertRaises(ValueError):
                    plan_russian_plurals(root, {'plurals': {'setting': forms}})

    def test_generated_helper_tampering_blocks_repeat(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture(root)
            changes = plan_russian_plurals(root)
            paths = apply_overlay(root, changes=changes)
            files = {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
            stamp = root / '.git/teleru-localization.json'
            stamp.parent.mkdir()
            stamp.write_text(json.dumps({'inputs': 'fixture', 'files': files}))
            header = root / 'Telegram/SourceFiles/tele/tele_russian_plural.h'
            header.write_bytes(header.read_bytes() + b'changed\r\n')
            with patch.object(translate_ru, 'fingerprint', return_value='fixture'), patch.object(translate_ru.subprocess, 'check_output', return_value='.git/teleru-localization.json'), patch.object(sys, 'argv', ['translate_ru.py', str(root)]):
                with self.assertRaisesRegex(ValueError, 'Localized source changed'):
                    translate_ru.main()

    def test_native_russian_plural_index(self):
        compiler = shutil.which('g++') or shutil.which('clang++')
        msvc = False
        if not compiler and os.name == 'nt':
            compiler = shutil.which('cl')
            locator = Path(os.environ.get('ProgramFiles(x86)', 'C:/Program Files (x86)')) / 'Microsoft Visual Studio/Installer/vswhere.exe'
            if not compiler and locator.is_file():
                found = subprocess.check_output([str(locator), '-latest', '-products', '*', '-requires', 'Microsoft.VisualStudio.Component.VC.Tools.x86.x64', '-find', 'VC/Tools/MSVC/**/bin/Hostx64/x64/cl.exe'], text=True).splitlines()
                compiler = found[0] if found else None
            msvc = compiler is not None
        if not compiler:
            self.skipTest('No C++ compiler is installed')
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture(root)
            changes = plan_russian_plurals(root)
            header = root / 'Telegram/SourceFiles/tele/tele_russian_plural.h'
            header.write_text(changes[header], encoding='utf-8')
            cases = {0: 2, 1: 0, 2: 1, 4: 1, 5: 2, 11: 2, 12: 2, 14: 2, 21: 0, 22: 1, 25: 2, 101: 0, 111: 2, -1: 0, -12: 2, -22: 1, -2147483648: 2}
            assertions = '\n'.join(f'static_assert(Tele::RussianPluralIndex({count}) == {index});' for count, index in cases.items())
            program = root / 'test.cpp'
            program.write_text('#include "Telegram/SourceFiles/tele/tele_russian_plural.h"\n' + assertions + '\nint main() { return 0; }\n')
            if msvc:
                subprocess.run([compiler, '/nologo', '/std:c++17', '/c', str(program), '/Fo' + str(root / 'test.obj')], check=True, capture_output=True)
                return
            executable = root / 'test.exe'
            subprocess.run([compiler, '-std=c++17', str(program), '-o', str(executable)], check=True, capture_output=True)
            subprocess.run([str(executable)], check=True)


if __name__ == '__main__':
    unittest.main()
