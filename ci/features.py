#!/usr/bin/env python3
"""regenerate docs/features.md from the patch rows in docs/releases.md, grouped by settings page.

the intro and the prose above and below each page's table are kept from the current features.md,
so only the tables are rewritten. a page that isn't there yet gets the default text below.
"""

import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_REPO = os.path.join(HERE, '..')
PAGES = ('interface', 'chats', 'messages', 'sending', 'notifications', 'menus', 'privacy',
         'profiles and ids', 'bots', 'debug', 'server', 'backup', 'updates', 'everywhere', 'other')
TABLE = ('| # | what it does | toggle |', '|---|---|---|')

INTRO = """# features

every tele patch, grouped by the settings page that holds its switch. [releases](releases.md) has the same rows by the release that brought them.

everything tele adds lives in settings → tele, right below the language row, grouped into pages. the search at the top of the page, and the main settings search, find every tele setting. right-click any of them to copy a link that opens it.

backup exports your tele settings to a file you can give to anyone, and imports one with a preview of what changes. it covers tele's switches and lists, not telegram's own settings (like interface scale) or data kept per account (local pins, pinned sets, bookmarks, local folders). to move everything to another folder or pc, copy the whole `tdata` folder next to tele.

"toggle" is where the switch is and its default. `always on` has no switch, `with N` follows the switch of patch N.

more about some of them: [title bar template](title-template.md), [link cleaner](link-cleaner.md), [launch flags](launch-flags.md), [tele server](server.md)."""

HEADS = {page: f'settings → tele → {page}.' for page in PAGES} | {
    'everywhere': 'always on, or without a switch of their own.',
    'other': 'everything else.',
}

TAILS = {
    'profiles and ids': """### gift studio

the gift studio builds any collectible from real parts and exports it, the grid builder lays out a whole profile of gifts, and fake upgrades spin any upgradable gift without spending anything (201, 209 and 202 above). open them from this page or from a gift's menu.

tgs files exported from the gift studio carry an invisible mark that says they were made with tele's gift studio. it holds nothing about you: no user, account, device or time.""",
}


def load_notes(repo):
    sys.path.insert(0, os.path.join(repo, 'ci'))
    import notes
    return notes


def parse(notes, text):
    rows = []
    for line in text.splitlines():
        match = notes.ROW.match(line.strip())
        if match:
            number, path, what, where = match.groups()
            rows.append((int(number), path, what, where))
    return rows


def kept(path):
    try:
        with open(path, encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        return INTRO, {}, {}
    parts = re.split(r'^## (.+)$', text, flags=re.M)
    heads, tails = {}, {}
    for title, body in zip(parts[1::2], parts[2::2]):
        lines = body.strip('\n').split('\n')
        start = next((index for index, line in enumerate(lines) if line.startswith('|')), len(lines))
        end = start
        while end < len(lines) and lines[end].startswith('|'):
            end += 1
        heads[title.strip()] = '\n'.join(lines[:start]).strip()
        tails[title.strip()] = '\n'.join(lines[end:]).strip()
    return parts[0].strip(), heads, tails


def render(notes, rows, intro, heads, tails):
    wheres = {number: where for number, _, _, where in rows}
    pages = {page: [] for page in PAGES}
    for number, path, what, where in sorted(rows):
        pages[notes.category(where, wheres)].append(f'| [{number}](../{path}) | {what} | {where} |')
    out = [intro]
    for page, lines in pages.items():
        if not lines:
            continue
        out += ['', f'## {page}', '']
        head = heads.get(page, HEADS[page])
        if head:
            out += [head, '']
        out += [*TABLE, *lines]
        tail = tails.get(page, TAILS.get(page, ''))
        if tail:
            out += ['', tail]
    return '\n'.join(out) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--repo', default=DEFAULT_REPO)
    parser.add_argument('--out', default='', help='file to write, docs/features.md in the repo by default')
    args = parser.parse_args()
    notes = load_notes(args.repo)
    out = args.out or os.path.join(args.repo, 'docs', 'features.md')
    with open(os.path.join(args.repo, 'docs', 'releases.md'), encoding='utf-8') as file:
        rows = parse(notes, file.read())
    numbers = [number for number, *_ in rows]
    assert len(numbers) == len(set(numbers)), 'a patch has two rows in releases.md'
    text = render(notes, rows, *kept(out))
    with open(out, 'w', encoding='utf-8', newline='\n') as file:
        file.write(text)
    count = sum(1 for line in text.splitlines() if notes.ROW.match(line))
    print(f'{count} rows from {len(rows)} in releases.md -> {out}')


if __name__ == '__main__':
    main()
