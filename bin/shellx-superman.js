#!/usr/bin/env node
console.log(`
  ╔══════════════════════════════════════════╗
  ║   ShellX — Superman Mode                ║
  ║   Multi-Agent Cognitive Diagnostic      ║
  ╚══════════════════════════════════════════╝
`);

const intent = process.argv.slice(2).join(' ');

if (!intent) {
  console.log('Usage: shellx-superman "<intent>"');
  console.log('Example: shellx-superman "full diagnostic"');
  process.exit(1);
}

console.log(`  Intent:  "${intent}"`);
console.log(`  Mode:    Superman (multi-agent orchestration)\n`);

console.log('  [Superman] Loading LinkX...');
console.log('  [Superman] Confirming project goal...');
console.log('  [Superman] Scanning codebase...');
console.log('  [Superman] Reconciling triple context...');
console.log('  [Superman] Running workers safely...');
console.log('  [Superman] Creating Stone...');
console.log('  [Superman] Updating LinkX...\n');

const { run } = require('./runner');
run('doctor');
