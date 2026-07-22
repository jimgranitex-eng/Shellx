import { existsSync } from 'fs';
import { join } from 'path';

export async function verifyCommand() {
  console.log('\n✅ Verifying ShellX installation...');
  const cwd = process.cwd();

  const checks = [
    {
      name: '.linkx directory',
      path: join(cwd, '.linkx'),
    },
    {
      name: '.reports directory',
      path: join(cwd, '.reports'),
    },
    {
      name: '.stones directory',
      path: join(cwd, '.stones'),
    },
    {
      name: 'LinkX core.json',
      path: join(cwd, '.linkx', 'core.json'),
    },
  ];

  let passed = 0;
  let failed = 0;

  console.log('\nVerification Results:\n');
  checks.forEach((check) => {
    const exists = existsSync(check.path);
    const status = exists ? '✅' : '❌';
    console.log(`${status} ${check.name}`);
    if (exists) passed++;
    else failed++;
  });

  console.log(`\n${passed}/${checks.length} checks passed`);
  if (failed > 0) {
    console.log(`\n⚠️  Some checks failed. Run: shellx init\n`);
  } else {
    console.log('\n🎯 All checks passed! ShellX is ready to use.\n');
  }
}
