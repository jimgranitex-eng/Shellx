# ShellX — Quickstart Guide

## Install

```bash
npm install -g shellx-dev-cli
```

## Commands

```bash
shellx init
shellx linkx init
shellx linkx scan
shellx linkx show
shellx linkx timeline
shellx verify
shellx report
shellx --xx "your intent here"
```

## Publish flow

If you are developing ShellX locally:

```bash
git checkout feature/cli-implementation
npm install
npm version 3.0.0
npm publish --access public
```
