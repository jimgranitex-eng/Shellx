#!/usr/bin/env node
const { run } = require('./runner');

const args = process.argv.slice(2);
let mode = args[0] || 'doctor';
if (mode.startsWith('-')) mode = mode.replace(/^-+/, '');

const valid = ['doctor','launcher','preflight','daemon-once','brain','bridge','linkx','report','help'];

if (mode === 'help') {
  console.log(`
ShellX Dev CLI — Cognitive Developer Engine

Usage:
  shellx-dev-cli <mode> [options]

Modes:
  doctor           Run main diagnostic flow
  launcher         Run launcher flow
  preflight        Fast alignment check
  daemon-once      Supervised single cycle
  brain            Repo sweep and candidate scan
  bridge           Start local HTTP helper on port 8765
  report           Run doctor and show latest report
  linkx init       Initialize LinkX memory
  linkx scan       Scan project state into LinkX

Examples:
  shellx-dev-cli doctor
  shellx-dev-cli report
  shellx-dev-cli linkx init
`);
  process.exit(0);
}

const pythonModes = ['doctor','launcher','preflight','daemon-once','brain','bridge'];
if (pythonModes.includes(mode)) {
  run(mode);
} else if (mode === 'report') {
  const fs = require('fs');
  const path = require('path');
  const reportsDir = path.join(process.cwd(), '.reports');
  console.log('ShellX: Running doctor to generate report...');
  run('doctor');
} else if (mode === 'linkx') {
  const sub = args[1] || 'help';
  const linkxDir = process.cwd() + '/.shellx';
  switch (sub) {
    case 'init':
      const fs = require('fs');
      fs.mkdirSync(linkxDir, { recursive: true });
      fs.writeFileSync(linkxDir + '/goal.json', JSON.stringify({ goal: '', created: new Date().toISOString() }, null, 2));
      console.log('LinkX initialized at ' + linkxDir);
      break;
    case 'scan':
      console.log('LinkX scan — analyzing project state...');
      run('preflight');
      break;
    default:
      console.log('Usage: shellx-dev-cli linkx init|scan');
  }
} else {
  console.log('Unknown mode: ' + mode);
  console.log('Run shellx-dev-cli --help for usage');
}
