# Contributing to ShellX

Thank you for your interest in contributing to **ShellX**, the cognitive developer engine that powers diagnostics, automation, and multi‑agent workflows inside KickerOS.

ShellX has evolved through several generations:

- **V1** – Simple report generator  
- **V2** – Multi‑agent expansion  
- **V3** – Cognitive reporting engine (this release)  
- **V4** – Planned modular standalone engine  

This document explains how to contribute safely and effectively.

---

# 🧭 Project Philosophy

ShellX is built on three principles:

1. **Human‑Readable Intelligence**  
   Everything ShellX outputs must be understandable at a glance.

2. **Deterministic Execution**  
   Pipelines must run in a predictable order, even when multi‑agent.

3. **Reversible Actions**  
   Every operation must produce a Stone (recovery snapshot).

---

# 🧱 Project Structure

```
shellx-core/          # V1 report engine
shellx-engine/        # V3 cognitive engine + pipelines
shellx-superman/      # All-systems diagnostic mode
shellx-workers/       # Deep audit, debug, architect, memory, autofix
shellx-reporting/     # Collector, merger, compressor, templates
shellx-linkx/         # Memory timeline
shellx-stones/        # Recovery snapshots
docs/                 # Documentation
```

---

# 🛠 How to Contribute

## 1. Fork the repository
Create your own fork and clone it locally.

## 2. Create a feature branch
```
git checkout -b feature/my-improvement
```

## 3. Follow the coding style
- TypeScript preferred  
- Keep functions small  
- Add comments for complex logic  
- Include GPL header in new files  

## 4. Add tests (V4 will include a test harness)

## 5. Submit a pull request
Include:
- What you changed  
- Why you changed it  
- Any breaking changes  
- Screenshots or logs if relevant  

---

# 🧩 Areas Where Help Is Needed

- V3 report templates  
- V4 modularization  
- VS Code extension  
- LinkX visualization  
- Stone timeline UI  
- Multi‑agent improvements  
- Documentation  

---

# 🛡 License

By contributing, you agree that your contributions will be licensed under the **GPL‑3.0** license.
