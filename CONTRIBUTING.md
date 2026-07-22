# Contributing to ShellX

Thank you for your interest in contributing to ShellX! 🎉

ShellX is an open-source cognitive developer engine licensed under **GPL-3.0**. We welcome contributions that improve the core engine, CLI, workers, documentation, and tooling.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Reporting Issues](#reporting-issues)
- [Style Guidelines](#style-guidelines)

---

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md). We are committed to keeping this project welcoming and respectful for everyone.

---

## Getting Started

### Fork & Clone

```bash
# Fork the repository on GitHub
# Then clone your fork:
git clone https://github.com/YOUR-USERNAME/Shellx.git
cd Shellx
```

### Install Dependencies

```bash
npm install
```

### Test the CLI

```bash
# Show version
node bin/shellx.js --version

# Run init
node bin/shellx.js init

# Test LinkX
node bin/shellx.js linkx init
node bin/shellx.js linkx show

# Test cognitive mode
node bin/shellx.js --xx "test"
```

---

## How to Contribute

### 🐛 Bug Fixes

1. **Check existing issues:**
   - Go to [GitHub Issues](https://github.com/jimgranitex-eng/Shellx/issues)
   - Search for your bug

2. **Create an issue if needed:**
   - Describe the bug clearly
   - Include reproduction steps
   - Add error output

3. **Submit a fix:**
   - Fork the repo
   - Create a branch: `fix/bug-description`
   - Make your changes
   - Test thoroughly
   - Submit a PR

### ✨ New Features

1. **Open an issue first:**
   - Describe the feature
   - Explain the use case
   - Label it `enhancement`

2. **Wait for feedback:**
   - Maintainers will review
   - Discuss approach

3. **Build the feature:**
   - Create a branch: `feature/feature-name`
   - Make changes
   - Add tests
   - Submit a PR

### 📚 Documentation

- Improvements to `docs/`, `README.md`, or code comments are always welcome
- Submit a PR directly — no issue required for docs-only changes

### 🎨 Website & Design

- Updates to `shellx-website/` welcome
- CSS/HTML improvements
- Documentation site enhancements

---

## Development Setup

### Project Structure

```
.
├── bin/
│   └── shellx.js              CLI executable
├── src/
│   ├── index.js               Main CLI router
│   └── commands/              Command implementations
│       ├── init.js
│       ├── linkx.js
│       ├── verify.js
│       └── report.js
├── docs/                      Documentation
├── shellx-website/            GitHub Pages website
├── tests/                     Test files (future)
├── package.json               Dependencies & scripts
└── README.md                  Main documentation
```

### Running Locally

```bash
# Install
npm install

# Run any command:
node bin/shellx.js init
node bin/shellx.js linkx show
node bin/shellx.js report
node bin/shellx.js --xx "test intent"

# Or use npm link for global access:
npm link
shellx --version
```

---

## Testing

### Manual Testing (Current)

```bash
# Test init flow
node bin/shellx.js init
node bin/shellx.js verify

# Test LinkX
node bin/shellx.js linkx init
node bin/shellx.js linkx scan
node bin/shellx.js linkx show
node bin/shellx.js linkx timeline

# Test reports
node bin/shellx.js report
node bin/shellx.js report --format detailed

# Test cognitive mode
node bin/shellx.js --xx "test"
```

### Automated Tests (Coming Soon)

```bash
npm test
```

---

## Submitting Changes

### Before You Submit

1. **Update from main:**
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Test thoroughly:**
   ```bash
   node bin/shellx.js init
   node bin/shellx.js verify
   npm test  # (when available)
   ```

3. **Update documentation:**
   - Update README if needed
   - Add comments to complex code
   - Update `docs/` if needed

### The PR Process

1. **Fork the repository**

2. **Create a feature branch:**
   ```bash
   git checkout -b feature/my-feature
   # or
   git checkout -b fix/my-bugfix
   ```

3. **Make focused commits:**
   ```bash
   git add src/commands/new-command.js
   git commit -m "feat: add new LinkX command"
   ```

4. **Keep commits clean:**
   - One feature per commit
   - Clear commit messages
   - Reference issues: `fixes #123`

5. **Push to your fork:**
   ```bash
   git push origin feature/my-feature
   ```

6. **Create a Pull Request:**
   - Title: clear and descriptive
   - Description: explain what and why
   - Reference issues
   - Provide context

### Pull Request Checklist

- [ ] Changes are focused and minimal
- [ ] Code is tested locally
- [ ] Documentation updated (README, docs/, comments)
- [ ] Commit messages are clear
- [ ] No breaking changes (or documented)
- [ ] Links to related issues
- [ ] Works with Node 16+

---

## Reporting Issues

### Bug Reports

Use [GitHub Issues](https://github.com/jimgranitex-eng/Shellx/issues) and include:

- 🐛 Clear title
- 📝 Steps to reproduce
- 🔍 Expected vs actual behavior
- 🖥️ OS, Node version
- 📋 Error output/logs

### Feature Requests

Include:

- 💡 Clear description
- 📌 Use case
- 🎯 Why it's needed
- 🔗 Related issues

### Security Issues

**Do NOT create a public issue.**

See [SECURITY.md](SECURITY.md) for reporting instructions.

---

## Style Guidelines

### JavaScript Code

```javascript
// ✅ Good
function initProject() {
  console.log('Initializing ShellX...');
  // Do work
}

// ✅ Good — descriptive names
const linkxPath = join(cwd, '.linkx', 'core.json');

// ✅ Good — comments for clarity
// Ensure LinkX is initialized before proceeding
function ensureLinkX() {
  if (!existsSync(linkxPath)) {
    throw new Error('LinkX not initialized');
  }
}
```

### File Organization

- One command per file
- Clear exports
- Descriptive function names
- Comments for complex logic

### Commit Messages

```
# ✅ Good
feat: add LinkX memory scan command
fix: resolve LinkX initialization race condition
docs: update quickstart guide

# ❌ Avoid
fixed stuff
wip
test
update
```

---

## Code Review Process

1. **Automated checks:**
   - GitHub Actions run tests
   - Code quality checks

2. **Manual review:**
   - Maintainers review code
   - Ask questions if needed
   - Request changes if necessary

3. **Approval & merge:**
   - Once approved, PR is merged
   - Squash-and-merge recommended

---

## Recognition

Contributors are recognized in:

- GitHub contributors page
- CHANGELOG.md
- Release notes
- (Coming soon: contributors page on shellx.dev)

---

## Getting Help

- 💬 Questions? Open a Discussion
- 🐛 Found a bug? Open an Issue
- 💡 Have an idea? Propose a feature
- 📖 Need help? Check CONTRIBUTING.md

---

## License

By contributing, you agree that your contributions will be licensed under the GPL-3.0 License.

---

Thank you for helping make ShellX better! 🚀
