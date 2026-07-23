<p align="center">
  <img src="logo-shellx-v5.jpg" width="220" alt="ShellX V5 Logo">
</p>
<p align="center"><em>Goal‑Driven Cognitive Developer Engine</em></p>

# ⚡ ShellX — Cognitive Developer Engine

ShellX is a goal‑driven cognitive developer engine that understands what you are building, why you are building it, and how far along you are. Using a persistent memory system called **LinkX**, ShellX performs safe, incremental, non‑destructive operations that align with your long‑term project goals.

## Quick Start

```bash
npm install -g shellx-dev-cli
shellx linkx init
shellx report
```

## Commands

| Command | Description |
|---------|-------------|
| `shellx doctor` | Run main diagnostic flow |
| `shellx launcher` | Run launcher flow |
| `shellx preflight` | Fast alignment check |
| `shellx daemon-once` | Supervised single cycle |
| `shellx brain` | Repo sweep and candidate scan |
| `shellx bridge` | Start local HTTP helper (experimental) |
| `shellx report` | Run doctor and show latest report |
| `shellx linkx init` | Initialize LinkX memory |
| `shellx linkx scan` | Scan project state into LinkX |
| `shellx activate <key>` | Activate ShellX Pro with license key |
| `shellx deactivate` | Deactivate current license |
| `shellx license status` | Show license status |
| `shellx ide detect` | Detect installed IDEs |
| `shellx ide list` | List supported IDEs |
| `shellx ide open <ide>` | Open project in IDE |
| `shellx --xx "<intent>"` | Explicit intent processing |
| `shellx-superman "<intent>"` | Full multi-agent diagnostic |

## Supported IDEs

VS Code, PyCharm, IntelliJ IDEA, WebStorm, Android Studio, Xcode, Sublime Text, Vim/Neovim

## License

ShellX (open source) is licensed under **GNU GPL v3**.
ShellX Pro is available under a commercial license.
