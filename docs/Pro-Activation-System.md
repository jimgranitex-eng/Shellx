# ShellX Pro — Activation System Design

ShellX Pro uses a simple, secure activation system to validate commercial licenses.

---

## Components

### 1. License Key

**Format:**

```
SHELLX-PRO-XXXX-XXXX-XXXX
```

- Generated per customer at purchase
- Unique per seat (Starter/Professional) or per organization (Enterprise)
- Stored locally in `~/.shellx/license.key`

---

### 2. Activation Command

Users activate ShellX Pro with:

```bash
shellx activate SHELLX-PRO-XXXX-XXXX-XXXX
```

This command:
- Validates the key format
- Stores it securely in `~/.shellx/`
- Unlocks Pro modules
- Enables Pro workers
- Enables Pro VS Code panels

---

### 3. Local Validation

ShellX Pro checks on startup:
- License key format
- Expiration date (if applicable)
- Signature integrity
- Local file integrity

No server required for local validation.

---

### 4. Optional Cloud Validation

For Enterprise customers:
- License keys validated via HTTPS
- Rate-limited per IP
- Signed responses to prevent tampering
- Supports seat management

---

### 5. Pro Module Unlocking

Once activated, the following become available:

| Module | Description |
|--------|-------------|
| `superman-pro` | Enhanced deep diagnostics |
| `architect-pro` | Deep architecture mapping |
| `memory-pro` | Memory graph analysis |
| `deep-audit-pro` | Comprehensive codebase audit |
| `autofix-pro` | Aggressive safe-mode autofixer |
| `verify-pro` | Multi-threaded verification pipeline |
| `timeline-pro` | Enterprise LinkX timeline |

---

## Security Notes

- Keys are hashed locally using SHA-256 before storage
- Plain-text keys are never written to logs
- Cloud validation uses HTTPS with certificate pinning
- Keys are not guessable (cryptographically random)
- License files are stored with restricted permissions (`chmod 600`)

---

## Deactivation

```bash
shellx deactivate
```

This removes the local license key and reverts to the open-source feature set.

---

## Roadmap (V4)

- Online license dashboard
- License revocation portal
- Seat management UI
- Usage analytics (opt-in only)
- Team license pools

---

*See [Pro-Onboarding-Email.md](Pro-Onboarding-Email.md) for the customer onboarding flow.*
