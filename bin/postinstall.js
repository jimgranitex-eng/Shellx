#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const bundleDir = path.join(__dirname, '..', 'bundle');
const reqFile = path.join(bundleDir, 'requirements.txt');

if (fs.existsSync(reqFile)) {
  console.log('ShellX: Installing Python dependencies...');
  try {
    execSync('pip install -r "' + reqFile + '"', { cwd: bundleDir, stdio: 'inherit' });
    console.log('ShellX: Python dependencies installed');
  } catch (e) {
    console.warn('ShellX: Could not install Python deps (pip not found?). Run manually: pip install -r "' + reqFile + '"');
  }
}
