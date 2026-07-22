# Contributing to ShellX

Thank you for your interest in contributing to ShellX.

ShellX is an open-source cognitive developer engine licensed under GPL-3.0. Contributions that improve the CLI, docs, website, or tooling are welcome.

---

## Getting Started

```bash
git clone https://github.com/jimgranitex-eng/Shellx.git
cd Shellx
npm install
```

Published CLI package:

```bash
npm install -g shellx-dev-cli
```

### Test the CLI

```bash
node bin/shellx.js --version
node bin/shellx.js init
node bin/shellx.js linkx init
node bin/shellx.js linkx show
node bin/shellx.js --xx "test"
```

---

## How to Contribute

### Bug Fixes

1. Check existing issues.
2. Open a new issue if needed.
3. Fork the repo.
4. Create a branch.
5. Submit a pull request.

### New Features

1. Open an issue first.
2. Describe the use case.
3. Fork the repo.
4. Create a feature branch.
5. Submit a PR with tests.

### Documentation

Docs-only improvements to `README.md`, `docs/`, or comments are always welcome.

---

## Development Setup

### Current project layout

```text
bin/
src/
src/commands/
docs/
shellx-website/
```

### Running locally

```bash
npm install
node bin/shellx.js init
node bin/shellx.js linkx show
node bin/shellx.js report
```

---

## Testing

### Manual testing

```bash
node bin/shellx.js init
node bin/shellx.js verify
node bin/shellx.js linkx init
node bin/shellx.js linkx scan
node bin/shellx.js linkx timeline
node bin/shellx.js report --format detailed
```

---

## Submitting Changes

- Keep commits focused
- Update docs when behavior changes
- Test locally before opening a PR
- Reference related issues when relevant

---

## Security

Do not report security issues publicly. See `SECURITY.md`.

---

## License

By contributing, you agree that your contributions will be licensed under GPL-3.0.
