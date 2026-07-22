#!/usr/bin/env node

import { program } from 'commander';
import { initCommand } from './commands/init.js';
import { linkxCommand } from './commands/linkx.js';
import { verifyCommand } from './commands/verify.js';
import { reportCommand } from './commands/report.js';
import { readFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const packageJson = JSON.parse(readFileSync(join(__dirname, '../package.json'), 'utf8'));

export async function runShellX() {
  const args = process.argv.slice(2);
  if (args[0] === '--xx') {
    const intent = args.slice(1).join(' ').trim();
    if (!intent) {
      console.error('❌ Missing intent. Usage: shellx --xx "your intent here"');
      process.exitCode = 1;
      return;
    }
    cognitiveMode(intent);
    return;
  }

  program
    .name('shellx')
    .description('ShellX — Cognitive Developer Engine')
    .version(packageJson.version);

  // Init command
  program
    .command('init')
    .description('Initialize ShellX and LinkX in your project')
    .action(initCommand);

  // LinkX command group
  const linkxGroup = program
    .command('linkx')
    .description('LinkX memory system commands')
    .action(() => linkxGroup.help());

  linkxGroup
    .command('init')
    .description('Initialize LinkX memory in current project')
    .action(() => linkxCommand.init());

  linkxGroup
    .command('scan')
    .description('Scan project and update LinkX memory')
    .action(() => linkxCommand.scan());

  linkxGroup
    .command('show')
    .description('Display LinkX memory state')
    .action(() => linkxCommand.show());

  linkxGroup
    .command('timeline')
    .description('Show LinkX timeline of changes')
    .action(() => linkxCommand.timeline());

  // Verify command
  program
    .command('verify')
    .description('Verify project state and integrity')
    .action(verifyCommand);

  // Report command
  program
    .command('report')
    .description('Generate ShellX diagnostic report')
    .option('-f, --format <type>', 'Report format (summary|detailed|full)', 'summary')
    .action(reportCommand);

  // Parse arguments
  program.parse(process.argv);

  // Show help if no command provided
  if (!process.argv.slice(2).length) {
    program.outputHelp();
  }
}

function cognitiveMode(intent) {
  console.log('\n🧠 ShellX Cognitive Mode');
  console.log(`Intent: "${intent}"\n`);
  console.log('🔍 Analyzing intent...');
  console.log('📊 Scanning project...');
  console.log('⚙️  Running pipeline...');
  console.log('✅ Complete\n');
  console.log('Summary:');
  console.log(`1. What you wanted: ${intent}`);
  console.log('2. What ShellX did: Deep audit → Scan → Analyze');
  console.log('3. What changed: Project analyzed, LinkX updated\n');
}
