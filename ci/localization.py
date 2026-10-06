#!/usr/bin/env python3
import argparse
import bisect
import collections
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
import web_resources

ROOT = Path(__file__).resolve().parent.parent
LEXER = re.compile(
    r'//[^\n]*|/\*.*?\*/|\'(?:\\.|[^\'\\])*\''
    r'|(?:u8|u|U|L)?R"(?P<delimiter>[^\s()\\]{0,16})\((?P<raw>.*?)\)(?P=delimiter)"'
    r'|(?P<prefix>u8|u|U|L)?"(?P<normal>(?:\\.|[^"\\])*)"', re.S)
PLACEHOLDERS = re.compile(r"%(?:L?\d+|n|%)")
EXTENSIONS = {".cpp", ".h", ".mm"}


@dataclass(frozen=True)
class Literal:
    start: int
    end: int
    text: str
    prefix: str


def decode_cpp(text):
    escapes = {"n": "\n", "r": "\r", "t": "\t", "a": "\a", "b": "\b", "f": "\f", "v": "\v", "\\": "\\", '"': '"', "'": "'", "?": "?"}

    def replace(match):
        value = match.group(1)
        if value.startswith("\n") or value.startswith("\r\n"):
            return ""
        if value in escapes:
            return escapes[value]
        if value.startswith(("x", "u", "U")):
            return chr(int(value[1:], 16))
        if value[0] in "01234567":
            return chr(int(value, 8))
        raise ValueError(f"Unsupported C++ escape: {value}")

    return re.sub(r"\\(\r?\n|x[0-9a-fA-F]+|u[0-9a-fA-F]{4}|U[0-9a-fA-F]{8}|[0-7]{1,3}|.)", replace, text)


def encode_cpp(text, prefix=""):
    if len(text) > 2000:
        return '\n'.join(encode_cpp(text[i:i + 1000], prefix) for i in range(0, len(text), 1000))
    encoded = json.dumps(text, ensure_ascii=False)
    encoded = re.sub(r"\\u00([0-9a-fA-F]{2})", lambda m: "\\" + format(int(m.group(1), 16), "03o"), encoded)
    return prefix + encoded


def literals(text):
    result = []
    for match in LEXER.finditer(text):
        normal, raw = match.group("normal"), match.group("raw")
        if normal is None and raw is None:
            continue
        value = decode_cpp(normal) if normal is not None else raw
        prefix = (re.match(r"(u8|u|U|L)?R", match.group()).group(1) or "") if raw is not None else (match.group("prefix") or "")
        current = Literal(match.start(), match.end(), value, prefix)
        if result:
            previous = result[-1]
            gap = re.sub(r"/\*.*?\*/|//[^\n]*", "", text[previous.end:current.start], flags=re.S)
            if not gap.strip():
                current = Literal(previous.start, current.end, previous.text + value, previous.prefix or prefix)
                result.pop()
        result.append(current)
    return result


def added_lines(tdesktop, baseline):
    output = subprocess.check_output(["git", "-C", str(tdesktop), "diff", "--unified=0", baseline, "--", "Telegram/SourceFiles"], text=True, encoding="utf-8")
    files = collections.defaultdict(set)
    path = None
    line_number = 0
    for line in output.splitlines():
        if line.startswith("+++ b/Telegram/SourceFiles/"):
            path = line[len("+++ b/Telegram/SourceFiles/"):]
        elif line.startswith("@@"):
            match = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@", line)
            line_number = int(match.group(1))
        elif line.startswith("+") and not line.startswith("+++"):
            if path:
                files[path].add(line_number)
            line_number += 1
        elif line.startswith(" "):
            line_number += 1
    return files


def collect(tdesktop, baseline):
    source = tdesktop / "Telegram/SourceFiles"
    if not source.is_dir():
        raise ValueError(f"Missing source directory: {source}")
    changes = added_lines(tdesktop, baseline)
    records = []
    for file in sorted(source.rglob("*")):
        if file.suffix not in EXTENSIONS or not file.is_file():
            continue
        path = file.relative_to(source).as_posix()
        own = path.startswith("tele/") or path.startswith("settings/settings_tele.")
        if not own and path not in changes:
            continue
        text = file.read_text(encoding="utf-8")
        lines = [-1] + [m.start() for m in re.finditer("\n", text)]
        for literal in literals(text):
            first = bisect.bisect_left(lines, literal.start)
            last = bisect.bisect_left(lines, literal.end)
            if not own and not changes[path].intersection(range(first, last + 1)):
                continue
            before = text[max(0, literal.start - 180):literal.start]
            after = text[literal.end:literal.end + 20]
            option = re.search(r"\.(name|description)\s*=\s*$", before)
            qstring = re.match(r"\s*_q\b", after) or re.search(r"(?:QStringLiteral|QString|_q)\(\s*$", before)
            if not option and not qstring:
                continue
            if not re.search(r"[A-Za-z]", literal.text):
                continue
            option_id = None
            field = None
            if option:
                ids = list(re.finditer(r"\.id\s*=\s*(kOption\w+)", text[:literal.start]))
                if ids:
                    option_id = ids[-1].group(1)
                    field = "name" if option.group(1) == "name" else "desc"
            technical = None
            if not option:
                if path == 'tele/tele_notices_section.cpp' and text.rfind('QString FilterId(', 0, literal.start) > text.rfind('QString FilterLabel(', 0, literal.start) and literal.start < text.find('\n}', text.find('QString FilterId(')):
                    technical = 'Persistent notice filter identifier'
                if re.search(r"\.(?:key|id|method|type|mime|settingsKey|defaultValue)\s*=\s*$", before):
                    technical = "Machine identifier, not display text"
                elif re.search(r"(?:\.value|\.insert|\.remove|\.contains|\.startsWith|\.endsWith|QLatin1String|QRegularExpression|QUrl|QStringConverter::encodingForName)\(\s*$", before):
                    technical = "Lookup key, URL or matching expression"
                elif re.search(r"(?:==|!=)\s*$", before) or re.match(r"\s*_q\s*(?:==|!=)", after):
                    technical = "Compared program value"
                elif re.search(r"\[\s*$", before) and re.match(r"\s*_q\s*\]", after):
                    technical = "Indexed storage key"
                elif re.search(r'UserAgentHeader\s*,\s*$', before):
                    technical = 'HTTP user-agent token'
            display = bool(option or re.search(r"(?:Lower|setTitle|setText|Show|addAction|addButton|single)\(\s*$", before))
            keyword = text.rfind('.keywords', 0, literal.start) > text.rfind('}', 0, literal.start)
            display = display or keyword
            if not display and re.fullmatch('[a-z_][a-z_0-9]*', literal.text) and re.search(r'\{\s*$', before) and re.match(r'\s*_q\s*,', after):
                technical = 'Aggregate lookup or configuration key'
            if not display and re.search(r'(?:notify|MenuRowId|Tagged|addSection|MenuLayoutHides|Field|SetAppIcon|SetTrayIcon|FileWriteDescriptor|router\.add|\.set)\(\s*$', before):
                technical = 'Protocol, registry or persistent setting identifier'
            records.append({"file": path, "line": first, "start": literal.start, "end": literal.end, "source": literal.text, "prefix": literal.prefix, "option": option_id, "field": field, "technical": technical, "display": display})
    if not records or not any(r["file"] == "tele/tele_options.cpp" for r in records):
        raise ValueError("No tele options found; apply the pinned patch queue first")
    return records + web_resources.collect(tdesktop)


def load_catalog(path):
    def unique(pairs):
        data = {}
        for key, value in pairs:
            if key in data:
                raise ValueError(f"Duplicate catalog key: {key}")
            data[key] = value
        return data

    data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique)
    def merge(target, addition):
        for key, value in addition.items():
            if isinstance(value, dict) and isinstance(target.get(key), dict):
                merge(target[key], value)
            else:
                target[key] = value

    for supplement in sorted((path.parent / "ru").glob("*.json")):
        merge(data, json.loads(supplement.read_text(encoding="utf-8"), object_pairs_hook=unique))
    if data.get("schema") != 1 or data.get("language") != "ru":
        raise ValueError("Unsupported localization catalog")
    return data


def resolve(record, catalog):
    source = record["source"]
    if record.get("technical"):
        return "ignored", None
    if not record.get('display') and source in catalog.get('machine', {}).get(record['file'], {}):
        return 'ignored', None
    if record["option"]:
        entry = catalog.get("options", {}).get(record["option"], {}).get(record["field"])
        if isinstance(entry, dict) and entry.get("source") == source:
            return "translated", entry["translation"]
        return "missing", None
    context = catalog.get("contexts", {}).get(record["file"], {})
    if source in context:
        return "translated", context[source]
    ignored = catalog.get("ignored", {}).get(record["file"], {})
    if source in ignored:
        if not isinstance(ignored[source], str) or not ignored[source].strip():
            raise ValueError("Every ignored technical literal needs a reason")
        if record.get('display'):
            if source in catalog['strings']:
                return 'translated', catalog['strings'][source]
            return 'missing', None
        return "ignored", None
    if source in catalog["strings"]:
        return "translated", catalog["strings"][source]
    return "missing", None


def validate_translation(source, translated):
    if not isinstance(translated, str) or not translated.strip():
        raise ValueError("Translation is empty")
    if sorted(PLACEHOLDERS.findall(source)) != sorted(PLACEHOLDERS.findall(translated)):
        raise ValueError(f"Changed placeholders: {source!r} -> {translated!r}")


def audit(records, catalog):
    missing = []
    invalid = []
    replacements = collections.defaultdict(list)
    ignored = 0
    for record in records:
        status, translated = resolve(record, catalog)
        if status == "missing":
            missing.append(record)
        elif status == "ignored":
            ignored += 1
        else:
            try:
                validate_translation(record["source"], translated)
            except ValueError as error:
                invalid.append(record | {"error": str(error)})
                continue
            replacements[record["file"]].append(record | {"translation": translated})
    count = len(records) - ignored
    translated = sum(map(len, replacements.values()))
    report = {"schema": 1, "scope": "tele QString candidates, option metadata and tele_html HTML/JavaScript literals; technical literals explicitly excluded, not a runtime UI guarantee", "total": count, "translated": translated, "ignored": ignored, "coverage": round(100 * translated / count, 4) if count else 0, "missing": missing, "invalid": invalid}
    return report, replacements


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def apply(tdesktop, replacements):
    for relative, records in replacements.items():
        file = tdesktop / "Telegram" / relative if relative.startswith('Resources/') else tdesktop / "Telegram/SourceFiles" / relative
        raw = file.read_bytes()
        newline = "\r\n" if b"\r\n" in raw else "\n"
        text = raw.decode("utf-8").replace("\r\n", "\n")
        for record in sorted(records, key=lambda r: r["start"], reverse=True):
            encoded = web_resources.encode(record['translation'], record['kind']) if record.get('kind') else encode_cpp(record["translation"], record["prefix"])
            text = text[:record["start"]] + encoded + text[record["end"]:]
        file.write_bytes(text.replace("\n", newline).encode("utf-8"))


def run(tdesktop, catalog_path, report_path, inventory_path=None, apply_changes=False, baseline=None):
    baseline = baseline or json.loads((ROOT / "TELE_UPSTREAM.json").read_text())["tdesktop"]
    records = collect(tdesktop, baseline)
    catalog = load_catalog(catalog_path)
    report, replacements = audit(records, catalog)
    write_json(report_path, report)
    if inventory_path:
        write_json(inventory_path, records)
    print(f"Localization: {report['translated']}/{report['total']} candidate occurrences ({report['coverage']:.2f}%), {report['ignored']} technical occurrences excluded")
    if report["missing"] or report["invalid"]:
        print(f"Publication blocked: {len(report['missing'])} missing, {len(report['invalid'])} invalid. Report: {report_path}", file=sys.stderr)
        return False
    if apply_changes:
        apply(tdesktop, replacements)
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tdesktop", type=Path)
    parser.add_argument("--catalog", type=Path, default=ROOT / "i18n/ru.json")
    parser.add_argument("--report", type=Path, default=ROOT / "localization-report.json")
    parser.add_argument("--inventory", type=Path)
    parser.add_argument("--baseline")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    return 0 if run(args.tdesktop.resolve(), args.catalog, args.report, args.inventory, args.apply, args.baseline) else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"Localization failed: {error}", file=sys.stderr)
        sys.exit(1)
