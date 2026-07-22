# ShellX — Quickstart Guide

Get up and running with ShellX in under 5 minutes.

---

## Prerequisites

- Node.js 16+
- npm
- A terminal
- A Git project (recommended)

---

## Installation

### Option 1 — Global Install

```bash
npm install -g shellx-dev-cli
```

### Option 2 — Local Development

```bash
git clone https://github.com/jimgranitex-eng/Shellx.git
cd Shellx
npm install
node bin/shellx.js --version
```

### Option 3 — npm link

```bash
npm link
shellx --version
```

---

## First Steps

### 1. Initialize ShellX

```bash
shellx init
```

This creates:
- `.linkx/` — LinkX memory system
- `.reports/` — Generated reports
- `.stones/` — Snapshot checkpoints

### 2. Initialize LinkX

```bash
shellx linkx init
```

### 3. Verify Installation

```bash
shellx verify
```

You should see all checks pass.

---

## Core Commands

### Cognitive Mode

```bash
shellx --xx "analyze the project structure"
```

### LinkX Commands

```bash
shellx linkx scan
shellx linkx show
shellx linkx timeline
```

### Reports

```bash
shellx report
shellx report --format detailed
shellx report --format full
```

Reports are saved to `.reports/`.

---

## Workflow Example

```bash
shellx init
shellx linkx init
shellx --xx "Refactor the authentication module for better performance"
shellx linkx show
shellx report
shellx linkx timeline
```

---

## Output Structure

| Output | Location |
|--------|----------|
| Reports | `.reports/` |
| Stones | `.stones/` |
| LinkX Memory | `.linkx/core.json` |

---

## Troubleshooting

### `shellx: command not found`

```bash
npm install -g shellx-dev-cli
```

### LinkX not initialized

```bash
shellx init
shellx linkx init
```

---

## Next Steps

- [Commands](../shellx-website/docs/commands.html)
- [Pro Features](Pro-Features.md)
- [Contributing](../CONTRIBUTING.md)
