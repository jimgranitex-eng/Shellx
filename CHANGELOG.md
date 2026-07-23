# Changelog

All notable changes to ShellX are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [3.2.1] — 2026-07-23

### Added
- **README — downloads badge** for npm total downloads
- **README — license diagram** showing dual-licensing model (open source vs Pro)
- **README — Quick Examples** section with 6 real-world command examples
- **License key validation** — `SHELLX-PRO-XXXX-XXXX-XXXX` example key now rejected with friendly error message instead of generic "Invalid"

### Changed
- README badges expanded from 3 to 4 (added downloads)

---

## [3.2.0] — 2026-07-23

### Fixed
- **Quickstart Install** — corrected from `npm install -g shellx` → `npm install -g shellx-dev-cli`; removed "coming soon" label
- **`.npmignore`** — comprehensive rewrite excludes shellx-website/, docs/, tests/, .github/, *.pdf, *.zip, and logo-shellx-v5.jpg from npm tarball
- **Hardcoded CLI version** — banner now reads `pkg.version` from package.json instead of hardcoded `v3.1.0`
- **Activation key format** — CLI `--help` example updated from `PRO-XXXX-XXXX` to `SHELLX-PRO-XXXX-XXXX-XXXX` to match all documentation
- **README command table** — expanded from 17 to 23 commands across 4 logical groups (Core, LinkX, Licensing, IDE)
- **Missing quickstart.html** — created `shellx-website/docs/quickstart.html` from Quickstart.md content
- **Broken link in Quickstart.md** — updated `Commands Reference` from missing website path → `../README.md#commands`
- **`shellx-superman-pro` in Pro-Features.md** — added Pro-only annotation
- **Website install command** — corrected from `./install.sh` → `npm install` in index.html
- **CHANGELOG — added missing entries** for v3.0.1 through v3.1.4
- **shellx-website/README.md** — removed password gate documentation and "Private Access" wording

### Added
- **README badges** — npm version, CI status, and license badges at top of README
- **README License section** — now links directly to LICENSE (GPL) and LICENSE-PRO.md; adds GitHub Sponsors call-to-action
- **Package size reduction** — .npmignore rewrite reduces tarball by ~2.5MB by excluding website, marketing docs, and large assets

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [3.1.4] — 2026-07-23

### Changed
- Further test hardening for npm/gitignore checks

---

## [3.1.3] — 2026-07-23

### Fixed
- npm/gitignore test assertions to work from repo root

---

## [3.1.2] — 2026-07-23

### Changed
- Enhanced `.npmignore` to exclude build artifacts from npm tarball

---

## [3.1.1] — 2026-07-23

### Added
- Comprehensive soundness test suite: 39 tests covering all core modules
- Test for IDE usage output formatting

### Fixed
- IDE usage output formatting to not use `process.exit()` during `--help`

---

## [3.1.0] — 2026-07-23

### Added
- **ShellX Pro licensing engine** (`lib/license.js`) — key validation, machine binding, 14-day trial
- **IDE integration** (`lib/ide.js`) — detect/list/open 8 IDEs, VS Code actions
- **`shellx activate <key>`** — activate ShellX Pro with license key
- **`shellx deactivate`** — deactivate current license
- **`shellx license status`** — show license status
- **`shellx ide detect`** — detect installed IDEs
- **`shellx ide list`** — list supported IDEs
- **`shellx ide open <ide>`** — open project in IDE
- **`shellx ide vscode <action>`** — VS Code actions
- **`shellx --xx "<intent>"`** — explicit cognitive mode
- **`shellx-superman "<intent>"`** — full multi-agent diagnostic
- **CI/CD workflow** (`.github/workflows/ci.yml`) — automated testing
- `bin/postinstall.js` — framework/shellx directory setup on install

### Changed
- CLI surface expanded from 8 to 19 commands
- Version bumped from 3.0.2 to 3.1.0 (significant new surface)

---

## [3.0.2] — 2026-07-23

### Fixed
- `PROJECT_ROOT` type — changed to `Path()` object for path operations
- Prevents `TypeError` when resolving project root

---

## [3.0.1] — 2026-07-23

### Fixed
- Doctor crash when `rglob()` encounters files without read permission — wrapped in try/except
- Search roots limited to `CWD` to prevent scanning entire filesystem
- `package.json.repository.url` format for npm metadata

---

## [3.0.0] — 2026-07-23

### Added
- **ShellX V3 Cognitive Engine** — new `--xx` mode for human-readable 1-2-3 summaries
- **Cognitive compression** — extracts real intent from natural language messages
- **Full pipeline integration** — runs all workers, compresses outputs into a clean summary
- **LinkX update** on every run
- **Stone creation** after each pipeline execution
- **VS Code manifest** for extension scaffolding
- **Docs website** (`shellx-website/`) with quickstart, commands, and license pages
- `docs/` directory with Pro documentation suite:
  - `Pro-Pricing.md`, `Pro-Features.md`, `Pro-Enterprise.md`
  - `Pro-FAQ.md`, `Pro-Activation-System.md`, `Pro-Onboarding-Email.md`
  - `GitHub-Sponsors-Description.md`, `Stripe-Checkout-Description.md`
  - `Website-Full.md`, `Pricing-Calculator.md`, `Marketing-Page.md`
  - `CI-CD-Pipeline.md`, `Quickstart.md`
- `LICENSE-PRO.md` — commercial license for ShellX Pro
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`
- `.github/FUNDING.yml` — GitHub Sponsors configuration

### Changed
- `README.md` upgraded with professional badges, ShellX Pro section, and topics

---

## [2.0.0] — 2025-01-01

### Added
- **ShellX V2 — Superman Era** — multi-agent diagnostic engine
- `shellx-superman` command for deep audits
- Deep architecture mapping
- Memory graph analysis
- Safe-mode autofix
- Verification pipeline
- Stone snapshots
- LinkX timeline (basic)

---

## [1.0.0] — 2024-01-01

### Added
- **ShellX V1** — original single-command autofixer
- `shellx "message"` command
- Worker execution
- Report generation with timestamps
- Basic LinkX integration

---

*For ShellX Pro changelog, see the private repository.*
