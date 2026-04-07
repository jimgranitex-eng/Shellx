# ShellX CLI Help System

This is the text displayed when users run:

```
shellx help
```

---

# ShellX — Cognitive Developer Engine

```
Usage:
  shellx <command> [options]

Commands:
  <message>           Run classic ShellX report
  --xx <message>      Run Cognitive Engine (V3)
  preflight           Run environment checks
  report              Generate a standard report
  collect             Collect metadata
  look                View last report

Workers:
  deep-audit          Run deep audit worker
  debug               Run debug worker
  architect           Run architecture worker
  memory              Run memory worker
  autofix             Run safe-mode autofix
  verify              Run verification

Superman:
  shellx-superman     Run full diagnostic pipeline

LinkX:
  linkx timeline      View memory timeline
  linkx show <id>     Show entry
  linkx search <q>    Search memory

Stones:
  stone list          List Stones
  stone show <id>     Show Stone
  stone diff <id>     Diff Stones
  stone restore <id>  Restore Stone

Multi-Project:
  multi-project       Run across multiple repos

Pro (Commercial):
  activate            Activate ShellX Pro
  architect-pro       Pro architecture mapping
  memory-pro          Pro memory analysis
  superman-pro        Pro diagnostic engine

Help:
  help                Show this help message
```
