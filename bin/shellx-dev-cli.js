#!/usr/bin/env node
const { run } = require('./runner');
const license = require('../lib/license');
const ide = require('../lib/ide');
const xx = require('../lib/xx');
const path = require('path');
const fs = require('fs');
const pkg = require('../package.json');

const args = process.argv.slice(2);

function printHelp() {
  console.log(`
  ╔══════════════════════════════════════════╗
  ║   ShellX — Cognitive Developer Engine   ║
  ║   v${pkg.version}${' '.repeat(34-pkg.version.length)}║
  ╚══════════════════════════════════════════╝

  USAGE:
    shellx <command> [options]
    shellx "<intent>"              Natural-language intent
    shellx --xx "<intent>"         Explicit intent processing (V3)

  CORE:
    --help, -h        Show this help
    --version, -v     Show version
    init              Initialize project
    verify            System/environment check
    doctor            Run main diagnostic flow
    launcher          Run launcher flow
    preflight         Fast alignment check
    daemon-once       Supervised single cycle
    brain             Repo sweep and candidate scan
    bridge            Start local HTTP helper on port 8765
    report            Run doctor and show latest report

  LINKX MEMORY:
    linkx init        Initialize LinkX memory
    linkx scan        Scan project state into LinkX
    linkx show        Show memory           (planned)
    linkx timeline    Timeline view         (planned)
    linkx search      Search memory         (planned)
    linkx export      Export memory         (planned)
    linkx diff        Compare memory states (planned)
    linkx import      Import memory         (planned)
    linkx purge       Clear memory          (planned)
    linkx rebuild     Rebuild memory        (planned)

  STONES:
    stone list        List stones
    stone show        Show stone details    (planned)
    stone diff        Compare stones        (planned)
    stone restore     Restore snapshot      (planned)
    stone create      Create snapshot

  LICENSING:
    activate <key>    Activate ShellX Pro with license key
    deactivate        Deactivate current license
    license status    Show license status
    trial status      Show trial state
    trial reset       Reset trial
    license verify    Validate license      (planned)

  IDE INTEGRATION:
    ide detect        Detect installed IDEs
    ide list          List supported IDEs
    ide open <ide>    Open project in IDE
    ide vscode install  Install VS Code extensions
    ide vscode tasks  Show VS Code tasks    (planned)
    ide config        Show IDE config       (planned)
    ide repair        Fix IDE integration   (planned)

  COGNITIVE MODES:
    shellx --xx "<intent>"         XX Intent Processor (V3)
    shellx-superman "<intent>"     Multi-agent orchestration (V2)

  MORE INFO:
    See docs/Commands.md for the full 40-command reference with examples

  EXAMPLES:
    shellx --version
    shellx doctor
    shellx report
    shellx linkx init
    shellx linkx scan
    shellx activate SHELLX-PRO-XXXX-XXXX-XXXX
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

if (['--version', '-v', 'version'].includes(mode)) {
  console.log(pkg.version);
  process.exit(0);
}

const validCommands = ['doctor','launcher','preflight','daemon-once','brain','bridge','report','linkx','activate','deactivate','license','ide','init','verify','stone','trial'];

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

if (mode === 'init') {
  const shellxDir = path.join(process.cwd(), '.shellx');
  fs.mkdirSync(shellxDir, { recursive: true });
  console.log('ShellX project initialized at ' + shellxDir);
  process.exit(0);
}

if (mode === 'verify') {
  console.log('ShellX: Running system verification...');
  run('preflight');
  process.exit(0);
}

if (mode === 'trial') {
  const sub = args[1] || 'status';
  if (sub === 'status') {
    const result = license.startTrial();
    console.log(result.message);
    process.exit(0);
  }
  if (sub === 'reset') {
    const trialFile = path.join(process.cwd(), '.shellx', 'trial.json');
    try { fs.unlinkSync(trialFile); } catch {}
    console.log('Trial reset.');
    process.exit(0);
  }
  console.log('Usage: shellx trial status|reset');
  process.exit(1);
}

if (mode === 'stone') {
  const sub = args[1] || 'list';
  const stonesDir = path.join(process.cwd(), '.shellx', 'stones');
  if (sub === 'list') {
    fs.mkdirSync(stonesDir, { recursive: true });
    const files = fs.readdirSync(stonesDir).filter(f => f.endsWith('.json'));
    if (files.length === 0) {
      console.log('No stones found.');
    } else {
      console.log('Stones:');
      files.forEach(f => console.log('  ' + f));
    }
    process.exit(0);
  }
  if (sub === 'show' && args[2]) {
    const stoneFile = path.join(stonesDir, args[2]);
    if (fs.existsSync(stoneFile)) {
      console.log(fs.readFileSync(stoneFile, 'utf8'));
    } else {
      console.log('Stone not found: ' + args[2]);
    }
    process.exit(0);
  }
  if (sub === 'create') {
    const stone = {
      id: Date.now().toString(36),
      timestamp: new Date().toISOString(),
      title: args.slice(2).join(' ') || 'Manual stone',
    };
    fs.mkdirSync(stonesDir, { recursive: true });
    fs.writeFileSync(path.join(stonesDir, stone.id + '.json'), JSON.stringify(stone, null, 2));
    console.log('Stone created: ' + stone.id);
    process.exit(0);
  }
  console.log('Usage: shellx stone list|show <id>|create [title]|diff <id>|restore <id>');
  process.exit(1);
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
      console.log('Usage: shellx linkx init|scan|show|timeline|search|export|diff|import|purge|rebuild');
  }
} else {
  console.log('Unknown command: ' + mode);
  console.log('Run shellx --help for usage');
  process.exit(1);
}
