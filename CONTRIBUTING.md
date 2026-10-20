# Contributing to teleru

Thank you for contributing to **teleru**!

`teleru` maintains a complete Russian localization and signed release pipeline for [tele](https://github.com/nitreojs/tele) (a patch queue fork of [Telegram Desktop](https://github.com/telegramdesktop/tdesktop)).

---

## Areas of Contribution

### 1. Localization & Terminology (`i18n/`)
- Refining Russian translations, improving context descriptions, or fixing grammar/plurals.
- All translations live under `i18n/ru/`:
  - `i18n/ru/new-options.json`: Name and description for options declared via `kOption...`.
  - `i18n/ru/reviewed-settings.json`: Refined settings requiring strict contextual binding.
  - `i18n/ru/menus-and-search.json`: Menu actions, search phrases, and UI tokens.
  - `i18n/ru/reviewed-technical.json`: Technical identifiers and formats explicitly excluded from translation.
  - `i18n/ru/title-presets.json`: Window title templates and format presets.
- **Rules**:
  - Maintain exact placeholder variables (`%1`, `%2`, `%L1`, `%n`, `%%`).
  - Use proper Russian typography: quotes «...» and curly apostrophes.
  - Preserve source bindings: `source` must match upstream English exactly.

### 2. CI Tooling & Verification (`ci/`)
- Automated audit tools (`ci/localization.py`, `ci/translate_ru.py`).
- Upstream patch application and version tracking (`ci/upstream.py`).
- Unit tests (`ci/tests/`).

### 3. Upstream Features & Fixes
- Enhancements and bug fixes to the underlying `tele` codebase should adhere to upstream standards documented in [docs/conventions.md](docs/conventions.md) and [docs/architecture.md](docs/architecture.md).

---

## Local Development Workflow

1. **Prerequisites**:
   - Python 3.11+
   - Node.js 18+
   - Git

2. **Install CI dependencies**:
   ```powershell
   npm ci --prefix ci --ignore-scripts
   python -m pip install -r ci/requirements.txt
   ```

3. **Run automated test suite**:
   ```powershell
   python -m unittest discover -s ci/tests -v
   ```
   All tests in `ci/tests/` must pass with zero failures.

4. **Verify localization coverage**:
   ```powershell
   python ci/localization.py C:\path\to\tdesktop
   ```
   The audit must report **100.00%** coverage with `0 missing` and `0 invalid` occurrences.

---

## Pull Request Checklist

Before opening a pull request, ensure:
- [ ] All 40 unit tests pass (`python -m unittest discover -s ci/tests -v`).
- [ ] Localization audit reports 0 missing and 0 invalid strings.
- [ ] Line endings match repository conventions (CRLF for Windows-targeted sources where applicable).
- [ ] Commit messages follow conventional commits (`feat: ...`, `fix: ...`, `docs: ...`, `chore: ...`).
- [ ] No private keys, credentials, or transient build artifacts are committed.
