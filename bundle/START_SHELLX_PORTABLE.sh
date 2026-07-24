#!/usr/bin/env bash
# ShellX Portable Launcher (Linux/macOS)
# Usage: bash START_SHELLX_PORTABLE.sh [doctor|launcher|preflight|daemon-once|brain|bridge]
set -euo pipefail

MODE="${1:-doctor}"
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

if command -v python3 &>/dev/null; then
    PYTHON=python3
elif command -v python &>/dev/null; then
    PYTHON=python
else
    echo "Python was not found on PATH."
    exit 1
fi

case "$MODE" in
    doctor)     $PYTHON core/ai_heart_doctor.py ;;
    launcher)   $PYTHON core/ai_heart_launcher.py ;;
    preflight)  $PYTHON -c "from core.ai_heart_system_utils import preflight_check; ok, issues = preflight_check(); print('PREFLIGHT_OK=', ok); print('\n'.join(issues) if issues else 'NO_ISSUES')" ;;
    daemon-once) $PYTHON core/ai_heart_daemon.py --once ;;
    brain)      $PYTHON core/ai_brain.py ;;
    bridge)     $PYTHON bridge/grok_http_bridge.py ;;
    *)
        echo "Usage: $0 [doctor|launcher|preflight|daemon-once|brain|bridge]"
        exit 1
        ;;
esac
