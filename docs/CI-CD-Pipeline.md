# ShellX — CI/CD Pipeline (GitHub Actions)

Recommended CI/CD configuration for ShellX and ShellX Pro projects.

---

## CI Pipeline — Test & Lint

Save as `.github/workflows/ci.yml` in your repository:

```yaml
name: ShellX CI

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - name: Lint
        run: npm run lint

      - name: Test
        run: npm test
```

---

## CD Pipeline — Release Build

Save as `.github/workflows/release.yml`:

```yaml
name: ShellX Release

on:
  push:
    tags:
      - "v*.*.*"

jobs:
  release:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - name: Build
        run: npm run build

      - name: Upload Release Artifact
        uses: actions/upload-artifact@v4
        with:
          name: shellx-build
          path: dist/

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          generate_release_notes: true
          files: dist/**
```

---

## ShellX Pro CI Pipeline (Private Repo)

For the private `ShellX-Pro` repository, add license validation to your pipeline:

```yaml
name: ShellX Pro CI

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - name: Validate Pro license structure
        run: npm run validate:license

      - name: Lint
        run: npm run lint

      - name: Test (with Pro modules)
        run: npm test
        env:
          SHELLX_PRO_TEST_KEY: ${{ secrets.SHELLX_PRO_TEST_KEY }}
```

---

## Recommended Branch Strategy

```
main          ← stable, protected branch
feature/*     ← new features
fix/*         ← bug fixes
release/*     ← release preparation
```

Pull requests require:
- CI passing
- At least one review approval
- No merge conflicts

---

## Notes

- Add Pro-only steps in the private `ShellX-Pro` repository pipeline
- Store license keys as GitHub Secrets, never in code
- Use `npm ci` instead of `npm install` in CI for reproducible builds
- Tag releases as `v3.0.0`, `v3.1.0`, etc. to trigger the CD pipeline

---

*See [CONTRIBUTING.md](../CONTRIBUTING.md) for development workflow guidelines.*
