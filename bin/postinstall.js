#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const bundleDir = path.join(__dirname, '..', 'bundle');
const reqFile = path.join(bundleDir, 'requirements.txt');

if (fs.existsSync(reqFile)) {
  console.log('ShellX: Installing Python dependencies...');
  const pipCandidates = ['python3 -m pip', 'pip3', 'pip', 'python -m pip'];
  let installed = false;
  for (const pipCmd of pipCandidates) {
    try {
      execSync(pipCmd + ' install -r "' + reqFile + '"', { cwd: bundleDir, stdio: 'inherit' });
      console.log('ShellX: Python dependencies installed');
      installed = true;
      break;
    } catch {}
  }
  if (!installed) {
    console.warn('ShellX: Could not install Python deps. Run manually: pip install -r "' + reqFile + '"');
  }
}
