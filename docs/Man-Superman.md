# SHELLX-SUPERMAN(1) — User Commands

## NAME
shellx-superman — Full multi-agent diagnostic engine

## SYNOPSIS
```
shellx-superman "<message>" [options]
```

## DESCRIPTION
Superman Mode runs the entire ShellX multi-agent pipeline:

- Smart input processing
- Deep audit
- Debug worker
- Architect worker
- Memory worker
- Safe-mode autofix
- Verification
- Stone creation
- LinkX update

## OPTIONS

### `--no-autofix`
Disable autofix stage.

### `--profile=<name>`
Use a custom diagnostic profile.

### `--strict`
Enforce strict parsing.

## EXAMPLES
```
shellx-superman "audit everything and stabilize the engine"
shellx-superman --no-autofix "run full diagnostics"
```

## FILES
```
~/.shellx/config.json
~/.shellx/stones/
```

## AUTHOR
James — Creator of ShellX
