const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const LICENSE_DIR = path.join(process.cwd(), '.shellx');
const LICENSE_FILE = path.join(LICENSE_DIR, 'license.json');
const PUBLIC_KEY = `-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwwPq1eFs0FfS1p3i6K9G
7zJcXk0h5sZ1v8fQ2t3y4r5t6y7u8i9o0p1q2w3e4r5t6y7u8i9o0p1q2w3e4r5t
-----END PUBLIC KEY-----`;

const TRIAL_DAYS = 14;

function getMachineId() {
  const { execSync } = require('child_process');
  try {
    if (process.platform === 'win32') {
      const result = execSync('wmic csproduct get uuid', { encoding: 'utf8', timeout: 5000 });
      const lines = result.split('\n').map(l => l.trim()).filter(l => l && !l.includes('UUID'));
      return lines[0] || 'unknown';
    } else {
      const result = execSync('cat /etc/machine-id 2>/dev/null || cat /var/lib/dbus/machine-id 2>/dev/null', { encoding: 'utf8', timeout: 5000 });
      return result.trim() || 'unknown';
    }
  } catch {
    return 'unknown-' + Date.now();
  }
}

function loadLicense() {
  try {
    if (fs.existsSync(LICENSE_FILE)) {
      return JSON.parse(fs.readFileSync(LICENSE_FILE, 'utf8'));
    }
  } catch {}
  return null;
}

function saveLicense(data) {
  fs.mkdirSync(LICENSE_DIR, { recursive: true });
  fs.writeFileSync(LICENSE_FILE, JSON.stringify(data, null, 2));
}

function verifyLicenseKey(key) {
  if (/^SHELLX-PRO-XXXX-XXXX-XXXX$/.test(key)) {
    throw new Error('This is an example key. Use the key provided at purchase.');
  }
  try {
    const parts = key.split('.');
    if (parts.length !== 2) return false;
    const data = Buffer.from(parts[0], 'base64').toString('utf8');
    const signature = Buffer.from(parts[1], 'base64');
    const verify = crypto.createVerify('SHA256');
    verify.update(data);
    return verify.verify(PUBLIC_KEY, signature);
  } catch {
    return false;
  }
}

function activate(key) {
  const existing = loadLicense();
  if (existing && existing.status === 'active') {
    return { success: true, message: 'Already activated', license: existing };
  }

  try {
    if (!verifyLicenseKey(key)) {
      return { success: false, message: 'Invalid license key' };
    }
  } catch (e) {
    return { success: false, message: e.message };
  }

  const license = {
    key: key,
    machine_id: getMachineId(),
    activated_at: new Date().toISOString(),
    status: 'active',
    type: 'pro',
    slots: 2,
  };
  saveLicense(license);
  return { success: true, message: 'Activated successfully', license };
}

function deactivate() {
  const existing = loadLicense();
  if (!existing) {
    return { success: false, message: 'No active license found' };
  }
  saveLicense({ ...existing, status: 'inactive', deactivated_at: new Date().toISOString() });
  return { success: true, message: 'Deactivated successfully' };
}

function status() {
  const license = loadLicense();
  if (!license) {
    const trial = loadTrial();
    return {
      status: 'unlicensed',
      trial: trial || null,
      message: trial ? `Trial mode — ${TRIAL_DAYS} day trial active` : 'Not activated. Run shellx activate <key>',
    };
  }
  if (license.status === 'inactive') {
    return { status: 'inactive', message: 'License is inactive. Run shellx activate <key> to reactivate' };
  }
  return {
    status: 'active',
    license: {
      type: license.type,
      activated_at: license.activated_at,
      slots: license.slots,
    },
    message: `ShellX ${license.type === 'pro' ? 'Pro' : 'Community'} — Active`,
  };
}

function loadTrial() {
  const trialFile = path.join(LICENSE_DIR, 'trial.json');
  try {
    if (fs.existsSync(trialFile)) {
      return JSON.parse(fs.readFileSync(trialFile, 'utf8'));
    }
  } catch {}
  return null;
}

function startTrial() {
  let trial = loadTrial();
  if (trial) {
    const elapsed = Date.now() - new Date(trial.started_at).getTime();
    const remaining = Math.max(0, TRIAL_DAYS * 86400000 - elapsed);
    return {
      success: true,
      trial: true,
      remaining_days: Math.ceil(remaining / 86400000),
      message: `Trial mode — ${Math.ceil(remaining / 86400000)} days remaining`,
    };
  }
  trial = {
    started_at: new Date().toISOString(),
    machine_id: getMachineId(),
  };
  fs.mkdirSync(LICENSE_DIR, { recursive: true });
  fs.writeFileSync(path.join(LICENSE_DIR, 'trial.json'), JSON.stringify(trial, null, 2));
  return {
    success: true,
    trial: true,
    remaining_days: TRIAL_DAYS,
    message: `Trial started — ${TRIAL_DAYS} days remaining`,
  };
}

module.exports = { activate, deactivate, status, startTrial, loadLicense };
