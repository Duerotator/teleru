import bisect
import html
import json
import re
import subprocess
from html.parser import HTMLParser
from pathlib import Path

HELPER = Path(__file__).with_name('js_literals.cjs')


def html_literals(text):
    lines = [-1] + [m.start() for m in re.finditer('\n', text)]
    result = []

    class Parser(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=False)
            self.skipped = 0

        def position(self):
            line, column = self.getpos()
            return lines[line - 1] + 1 + column

        def handle_starttag(self, tag, attrs):
            if tag in ('script', 'style'):
                self.skipped += 1
            raw = self.get_starttag_text()
            for match in re.finditer(r'\b(?:placeholder|title|aria-label|alt)\s*=\s*([\"\'])(.*?)\1', raw, re.S):
                start = self.position() + match.start(2)
                result.append(dict(start=start, end=self.position() + match.end(2), source=html.unescape(match.group(2)), kind='html'))

        def handle_endtag(self, tag):
            if tag in ('script', 'style'):
                self.skipped -= 1

        def handle_data(self, data):
            if self.skipped or not data.strip():
                return
            value = data.strip()
            start = self.position() + len(data) - len(data.lstrip())
            result.append(dict(start=start, end=start + len(value), source=html.unescape(value), kind='html'))

    Parser().feed(text)
    for record in result:
        record['line'] = bisect.bisect_left(lines, record['start'])
    return result


def js_literals(text):
    result = subprocess.run(['node', str(HELPER)], input=text.encode('utf-8'), capture_output=True)
    if result.returncode:
        raise ValueError('JavaScript parsing failed; run npm ci --prefix ci. ' + result.stderr.decode('utf-8', errors='replace')[-1500:])
    return [r | {'kind': 'js'} for r in json.loads(result.stdout.decode('utf-8'))]


def collect(tdesktop):
    root = tdesktop / 'Telegram'
    resources = root / 'Resources/tele_html'
    if not resources.is_dir():
        raise ValueError('Missing tele HTML resources')
    records = []
    for file in sorted(resources.rglob('*')):
        if file.suffix not in ('.html', '.js'):
            continue
        text = file.read_text(encoding='utf-8')
        items = html_literals(text) if file.suffix == '.html' else js_literals(text)
        for item in items:
            if re.search('[A-Za-z]', item['source']):
                records.append({'technical': None} | item | {'file': file.relative_to(root).as_posix(), 'option': None, 'field': None, 'prefix': ''})
    return records


def encode(text, kind):
    return html.escape(text, quote=True) if kind == 'html' else json.dumps(text, ensure_ascii=False)
