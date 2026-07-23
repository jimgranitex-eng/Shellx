const { run } = require('../bin/runner');

const INTENT_KEYWORDS = {
  'stabilize': 'Stabilization — detecting regressions, hardening systems, locking dependencies',
  'optimize': 'Optimization — identifying bottlenecks, reducing latency, improving memory usage',
  'refactor': 'Refactoring — restructuring code without changing behavior',
  'analyze': 'Analysis — deep codebase inspection, dependency mapping, architecture review',
  'build': 'Build — compiling, bundling, preparing artifacts',
  'deploy': 'Deployment — CI/CD pipeline coordination, release management',
  'test': 'Testing — running test suites, checking coverage, validating behavior',
  'diagnose': 'Diagnosis — root cause analysis, error tracing, log inspection',
};

function classifyIntent(text) {
  const lower = text.toLowerCase();
  for (const [keyword, description] of Object.entries(INTENT_KEYWORDS)) {
    if (lower.includes(keyword)) {
      return { keyword, description };
    }
  }
  return { keyword: 'general', description: 'General cognitive operation' };
}

function handle(intent) {
  const { keyword, description } = classifyIntent(intent);
  console.log(`\n  ShellX XX Intent Processor`);
  console.log(`  ─────────────────────────`);
  console.log(`  Intent:    ${keyword}`);
  console.log(`  Context:   ${description}`);
  console.log(`  Request:   "${intent}"`);
  console.log(`\n  Running cognitive analysis...\n`);

  run('doctor');
}

module.exports = { handle, classifyIntent, INTENT_KEYWORDS };
