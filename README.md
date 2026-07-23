<p align="center">
  <img src="logo-shellx-v5.jpg" width="220" alt="ShellX V5 Logo">
</p>
<p align="center"><em>Goal‑Driven Cognitive Developer Engine</em></p>

<p align="center">
  <a href="https://www.npmjs.com/package/shellx-dev-cli"><img src="https://img.shields.io/npm/v/shellx-dev-cli" alt="npm"></a>
  <a href="https://github.com/jimgranitex-eng/Shellx/actions"><img src="https://img.shields.io/github/actions/workflow/status/jimgranitex-eng/Shellx/ci.yml?branch=main" alt="CI"></a>
  <a href="https://github.com/jimgranitex-eng/Shellx/blob/main/LICENSE"><img src="https://img.shields.io/github/license/jimgranitex-eng/Shellx" alt="License"></a>
</p>

# ⚡ ShellX — Cognitive Developer Engine

ShellX is a goal‑driven cognitive developer engine that understands what you are building, why you are building it, and how far along you are. Using a persistent memory system called **LinkX**, ShellX performs safe, incremental, non‑destructive operations that align with your long‑term project goals.

## Quick Start

```bash
npm install -g shellx-dev-cli
shellx linkx init
shellx report
```

## Commands

### Core Commands

| Command | Description |
|---------|-------------|
| `shellx "<intent>"` | Natural language intent (auto-detected) |
| `shellx doctor` | Run main diagnostic flow |
| `shellx launcher` | Run launcher flow |
| `shellx preflight` | Fast alignment check |
| `shellx daemon-once` | Supervised single cycle |
| `shellx brain` | Repo sweep and candidate scan |
| `shellx bridge` | Start local HTTP helper (experimental) |
| `shellx report` | Run doctor and show latest report |
| `shellx --xx "<intent>"` | Explicit cognitive mode (V3) |
| `shellx-superman "<intent>"` | Full multi-agent diagnostic (V2) |

### LinkX Memory

| Command | Description |
|---------|-------------|
| `shellx linkx init` | Initialize LinkX memory |
| `shellx linkx scan` | Scan project state into LinkX |

### Licensing (Pro)

| Command | Description |
|---------|-------------|
| `shellx activate <key>` | Activate ShellX Pro with license key |
| `shellx deactivate` | Deactivate current license |
| `shellx license status` | Show license status |

### IDE Integration

| Command | Description |
|---------|-------------|
| `shellx ide detect` | Detect installed IDEs |
| `shellx ide list` | List supported IDEs |
| `shellx ide open <ide>` | Open project in IDE |
| `shellx ide vscode <action>` | VS Code actions (open, install, info) |

## Supported IDEs

VS Code, PyCharm, IntelliJ IDEA, WebStorm, Android Studio, Xcode, Sublime Text, Vim/Neovim

## License

- **ShellX (open source)** — [GNU GPL v3](LICENSE)
- **ShellX Pro** — [Commercial license](LICENSE-PRO.md)

[Sponsor ShellX Pro on GitHub Sponsors](https://github.com/sponsors/jimgranitex-eng)
