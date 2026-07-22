# ShellX — Cognitive Developer Engine

ShellX is a goal-driven cognitive developer engine that helps you understand what you're building, why you're building it, and how far along you are. It uses a persistent memory system called **LinkX** to produce safe, incremental, traceable operations.

## npm package

```bash
npm install -g shellx-dev-cli
```

## CLI commands

```bash
shellx init
shellx linkx init
shellx linkx scan
shellx linkx show
shellx linkx timeline
shellx verify
shellx report
shellx --xx "analyze the project structure"
```

## What ShellX does

ShellX turns complex developer workflows into structured output:

- Summary Report
- Detailed Report
- Full Report
- LinkX memory entry
- Stone snapshot

---

## Core Concepts

### Triple-Context Engine
ShellX evaluates every request using three layers of context:

1. **Immediate Intent** — what you asked for
2. **Long-Term Goal** — stored in LinkX
3. **Actual Project State** — scanned from the codebase

ShellX reconciles all three before taking action, ensuring correctness, continuity, and safety.

### LinkX — Core Memory System
LinkX is the primary memory and goal engine of ShellX.
ShellX boots on top of LinkX and relies on it for context-aware execution.

If LinkX is unavailable, ShellX enters safe mode and refuses destructive operations.

---

## Installation examples

### Global install

```bash
npm install -g shellx-dev-cli
```

### Verify install

```bash
shellx --version
shellx init
shellx linkx scan
```

---

## In One Sentence

**ShellX is a cognitive developer engine that preserves long-term project goals, analyzes your codebase, and performs safe, incremental operations using a persistent memory system called LinkX.**
