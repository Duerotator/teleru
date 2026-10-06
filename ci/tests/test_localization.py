import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import localization as l
import web_resources as web


def record(source='Hello %1', **extra):
    return dict(file='tele/test.cpp', source=source, option=None, field=None, start=0, end=12, prefix='u', display=True, technical=None) | extra


class LocalizationTests(unittest.TestCase):
    def test_cpp_lexer_skips_comments_and_chars(self):
        text = '// "not a literal"\n u"Hello" /* comment */ u" world"_q; char a=\'x\';'
        self.assertEqual([x.text for x in l.literals(text)], ['Hello world'])

    def test_cpp_raw_and_escapes(self):
        items = l.literals('uR"tag(Hello\nworld)tag"_q; u"line\\n\\u0041\\x42\\103"_q;')
        self.assertEqual([x.text for x in items], ['Hello\nworld', 'line\nABC'])
        self.assertEqual(items[0].prefix, 'u')

    def test_cpp_roundtrip(self):
        value = 'Кавычки: " \\ %1\n\t\x01 и 🧡'
        self.assertEqual(l.literals(l.encode_cpp(value, 'u'))[0].text, value)

    def test_large_cpp_template_is_chunked(self):
        value = 'Строка с \\ и кавычкой " ' * 200
        encoded = l.encode_cpp(value, 'u')
        self.assertIn('\n', encoded)
        self.assertEqual(l.literals(encoded)[0].text, value)

    def test_placeholder_loss_blocks(self):
        for source, translation in [('Hello %1', 'Привет'), ('%1 %1', '%1'), ('%L1', '%1'), ('%n %%', '%n')]:
            with self.assertRaises(ValueError):
                l.validate_translation(source, translation)
        l.validate_translation('%1 %2', '%2 %1')

    def test_empty_translation_blocks(self):
        with self.assertRaises(ValueError):
            l.validate_translation('Hello', ' ')

    def test_changed_option_source_blocks(self):
        c = {'strings': {}, 'options': {'kOptionTest': {'name': {'source': 'Old', 'translation': 'Старое'}}}}
        self.assertEqual(l.resolve(record('New', option='kOptionTest', field='name'), c)[0], 'missing')

    def test_machine_token_beats_translation(self):
        c = {'strings': {'online': 'в сети'}}
        self.assertEqual(l.resolve(record('online', technical='Stored value'), c)[0], 'ignored')
        self.assertEqual(l.resolve(record('online'), c), ('translated', 'в сети'))

    def test_ignore_cannot_hide_new_display_string(self):
        c = {'strings': {}, 'ignored': {'tele/test.cpp': {'identifier': 'Storage key'}}}
        self.assertEqual(l.resolve(record('identifier'), c)[0], 'missing')
        self.assertEqual(l.resolve(record('identifier', display=False), c)[0], 'ignored')

    def test_audit_has_no_false_success(self):
        report, changes = l.audit([record(), record('New menu')], {'strings': {'Hello %1': 'Привет %1'}})
        self.assertEqual(report['coverage'], 50)
        self.assertEqual(len(report['missing']), 1)
        self.assertEqual(len(changes['tele/test.cpp']), 1)

    def test_failed_run_does_not_write_source(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            catalog = root / 'ru.json'
            catalog.write_text('{"schema":1,"language":"ru","strings":{}}')
            source = root / 'Telegram/SourceFiles/tele/test.cpp'
            source.parent.mkdir(parents=True)
            source.write_bytes(b'u"Hello %1"_q;\r\n')
            before = source.read_bytes()
            with patch.object(l, 'collect', return_value=[record()]):
                self.assertFalse(l.run(root, catalog, root / 'report.json', apply_changes=True, baseline='v1.0.0'))
            self.assertEqual(source.read_bytes(), before)

    def test_apply_preserves_crlf(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / 'Telegram/SourceFiles/tele/test.cpp'
            source.parent.mkdir(parents=True)
            source.write_bytes(b'u"Hello %1"_q;\r\n')
            r = record(end=11, translation='Привет %1')
            l.apply(root, {'tele/test.cpp': [r]})
            self.assertEqual(source.read_bytes(), 'u"Привет %1"_q;\r\n'.encode())

    def test_duplicate_catalog_key_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            file = Path(temporary) / 'ru.json'
            file.write_text('{"schema":1,"schema":1}')
            with self.assertRaises(ValueError):
                l.load_catalog(file)

    def test_html_only_visible_text(self):
        text = '<button id="send" title="Send">Send</button><script>const s="send"</script>'
        items = web.html_literals(text)
        self.assertEqual([r['source'] for r in items], ['Send', 'Send'])
        for item in items:
            self.assertEqual(text[item['start']:item['end']], item['source'])

    def test_js_offsets_unicode_and_windows_stdin(self):
        text = '// 🧡\nconst x = "Hello";\nspan("optional", "optional");'
        items = web.js_literals(text)
        self.assertEqual([r['source'] for r in items], ['Hello', 'optional', 'optional'])
        for item in items:
            self.assertEqual(json.loads(text[item['start']:item['end']]), item['source'])
        self.assertTrue(items[1]['technical'])
        self.assertFalse(items[2]['technical'])
        self.assertTrue(items[2]['display'])

    def test_js_regex_is_not_a_string(self):
        items = web.js_literals('const x = /["\']/; const y = "Send";')
        self.assertEqual([r['source'] for r in items], ['Send'])

    def test_dom_id_inventory_is_not_translated(self):
        items = web.js_literals('for (const id of ["send", "cancel"]) { els[id] = document.getElementById(id); }')
        self.assertTrue(all(r['technical'] for r in items))

    def test_new_js_templates_fail_closed(self):
        with self.assertRaises(ValueError):
            web.js_literals('const x = `Send ${name}`;')

    def test_real_catalog_loads(self):
        catalog = l.load_catalog(l.ROOT / 'i18n/ru.json')
        self.assertEqual(catalog['language'], 'ru')
        self.assertGreaterEqual(len(catalog['options']), 214)


if __name__ == '__main__':
    unittest.main()
