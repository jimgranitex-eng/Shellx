const path = require('path');
const fs = require('fs');
const { spawn } = require('child_process');

const BUNDLE_DIR = path.join(__dirname, '..', 'bundle');

function findPython() {
  const candidates = ['py -3', 'python3', 'python'];
  for (const cmd of candidates) {
    try {
      require('child_process').execSync(cmd + ' --version', { stdio: 'ignore' });
      return cmd.split(' ');
    } catch {}
  }
  return ['python'];
}

function run(mode) {
  const scriptMap = {
    doctor: 'core/ai_heart_doctor.py',
    launcher: 'core/ai_heart_launcher.py',
    preflight: ['-c', 'from core.ai_heart_system_utils import preflight_check; ok, issues = preflight_check(); print("PREFLIGHT_OK=", ok); print("\\n".join(issues) if issues else "NO_ISSUES")'],
    'daemon-once': 'core/ai_heart_daemon.py --once',
    brain: 'core/ai_brain.py',
    bridge: 'bridge/grok_http_bridge.py',
  };

  const target = scriptMap[mode];
  if (!target) {
    console.error('Unknown mode: ' + mode);
    process.exit(1);
  }

  const python = findPython();
  const args = Array.isArray(target) ? target : [target];

  const proc = spawn(python[0], [...python.slice(1), ...args], {
    cwd: BUNDLE_DIR,
    stdio: 'inherit',
    env: { ...process.env, PYTHONUNBUFFERED: '1' },
  });

  proc.on('exit', (code) => process.exit(code));
}

module.exports = { run };
