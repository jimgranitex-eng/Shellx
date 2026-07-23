#!/usr/bin/env node
const { run } = require('./runner');
const license = require('../lib/license');
const ide = require('../lib/ide');
const xx = require('../lib/xx');
const path = require('path');
const fs = require('fs');

const args = process.argv.slice(2);

function printHelp() {
  console.log(`
  ╔══════════════════════════════════════════╗
  ║   ShellX — Cognitive Developer Engine   ║
  ║   v3.1.0                                ║
  ╚══════════════════════════════════════════╝

  USAGE:
    shellx <command> [options]
    shellx "<intent>"              Run with natural language intent
    shellx --xx "<intent>"         Explicit intent processing

  COMMANDS:
    doctor           Run main diagnostic flow
    launcher         Run launcher flow
    preflight        Fast alignment check
    daemon-once      Supervised single cycle
    brain            Repo sweep and candidate scan
    bridge           Start local HTTP helper on port 8765
    report           Run doctor and show latest report

    linkx init       Initialize LinkX memory
    linkx scan       Scan project state into LinkX

    activate <key>   Activate ShellX Pro with license key
    deactivate       Deactivate current license
    license status   Show license status

    ide detect       Detect installed IDEs
    ide list         List supported IDEs
    ide open <ide>   Open project in IDE
    ide vscode <action>  VS Code actions

  SUPERMAN MODE:
    shellx-superman "<intent>"     Full multi-agent diagnostic

  EXAMPLES:
    shellx doctor
    shellx report
    shellx linkx init
    shellx linkx scan
    shellx activate PRO-XXXX-XXXX
    shellx ide detect
    shellx ide open vscode
    shellx --xx "stabilize the rendering pipeline"
    shellx-superman "full diagnostic"
  `);
}

function handleIntentMode(text) {
  console.log(`ShellX: Processing intent — "${text}"`);
  xx.handle(text);
}

if (args.length === 0) {
  printHelp();
  process.exit(0);
}

let mode = args[0];

if (mode === '--xx') {
  const intent = args.slice(1).join(' ');
  if (!intent) { console.log('Usage: shellx --xx "<intent>"'); process.exit(1); }
  handleIntentMode(intent);
  process.exit(0);
}

if (mode.startsWith('-') && mode !== '--help' && mode !== '-h') {
  if (!args[0].startsWith('--')) {
    handleIntentMode(args.join(' '));
    process.exit(0);
  }
}

if (['--help', '-h', 'help'].includes(mode)) {
  printHelp();
  process.exit(0);
}

const validCommands = ['doctor','launcher','preflight','daemon-once','brain','bridge','report','linkx','activate','deactivate','license','ide'];

if (!validCommands.includes(mode)) {
  handleIntentMode(args.join(' '));
  process.exit(0);
}

if (mode === 'activate') {
  const key = args[1];
  if (!key) { console.log('Usage: shellx activate <license-key>'); process.exit(1); }
  const result = license.activate(key);
  console.log(result.message);
  process.exit(result.success ? 0 : 1);
}

if (mode === 'deactivate') {
  const result = license.deactivate();
  console.log(result.message);
  process.exit(result.success ? 0 : 1);
}

if (mode === 'license') {
  const sub = args[1] || 'status';
  if (sub === 'status') {
    const result = license.status();
    console.log(result.message);
    if (result.license) {
      console.log(`  Type:      ${result.license.type}`);
      console.log(`  Activated: ${result.license.activated_at}`);
      console.log(`  Slots:     ${result.license.slots}`);
    }
    process.exit(0);
  }
  console.log('Usage: shellx license status');
  process.exit(1);
}

if (mode === 'ide') {
  ide.handle(args.slice(1));
  process.exit(0);
}

const pythonModes = ['doctor','launcher','preflight','daemon-once','brain','bridge'];
if (pythonModes.includes(mode)) {
  run(mode);
} else if (mode === 'report') {
  console.log('ShellX: Running doctor to generate report...');
  run('doctor');
} else if (mode === 'linkx') {
  const sub = args[1] || 'help';
  const linkxDir = path.join(process.cwd(), '.shellx');
  switch (sub) {
    case 'init':
      fs.mkdirSync(linkxDir, { recursive: true });
      const goalFile = path.join(linkxDir, 'goal.json');
      if (!fs.existsSync(goalFile)) {
        fs.writeFileSync(goalFile, JSON.stringify({ goal: '', created: new Date().toISOString() }, null, 2));
      }
      console.log('LinkX initialized at ' + linkxDir);
      break;
    case 'scan':
      console.log('LinkX scan — analyzing project state...');
      run('preflight');
      break;
    default:
      console.log('Usage: shellx linkx init|scan');
  }
} else {
  console.log('Unknown command: ' + mode);
  console.log('Run shellx --help for usage');
  process.exit(1);
}
