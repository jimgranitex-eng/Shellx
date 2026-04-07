# SHELLX(1) — User Commands

## NAME
shellx — Cognitive Developer Engine

## SYNOPSIS
```
shellx [command] [options]
```

## DESCRIPTION
ShellX is a cognitive developer engine that analyzes your intent,
runs multi-agent diagnostics, and produces human-readable reports.

## COMMANDS

### `shellx "<message>"`
Run classic ShellX report.

### `shellx --xx "<message>"`
Run Cognitive Engine (V3).

### `shellx-superman "<message>"`
Run full diagnostic pipeline.

### `shellx preflight`
Run environment checks.

### `shellx report`
Generate a standard report.

### `shellx collect`
Collect metadata.

### `shellx look`
View last report.

## WORKERS
`deep-audit`, `debug`, `architect`, `memory`, `autofix`, `verify`

## LINKX
`linkx timeline`, `linkx show`, `linkx search`

## STONES
`stone list`, `stone show`, `stone diff`, `stone restore`

## PRO
`activate`, `architect-pro`, `memory-pro`, `superman-pro`

## FILES
```
~/.shellx/license.key
~/.shellx/config.json
```

## AUTHOR
James — Creator of ShellX

## COPYRIGHT
GPL-3.0 (Open Source Edition)  
ShellX Pro (Commercial Edition)
