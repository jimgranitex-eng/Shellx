#!/usr/bin/env python3
"""ShellX pipeline helper

Usage:
  python scripts/shellx_pipeline.py --report-dir build --target <path> --content-file <file>

Behavior:
- Runs scripts/preflight_check.py to produce preflight_before.json in report-dir
- If --target and --content-file are provided it writes the content into the target file (backing up original)
- Runs preflight again to produce preflight_after.json
- Produces a simple diff summary comparing the two reports and prints/writes a summary
- Optionally runs the deployed exe and captures stdout to report-dir/shellx_run.log

This is intentionally conservative: it will back up modified target files and restore them after the run.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

def run_preflight(report_path):
    cmd = [sys.executable, 'scripts/preflight_check.py', '--report', str(report_path)]
    print('Running:', ' '.join(cmd))
    subprocess.check_call(cmd)

def load_report(p):
    try:
        with open(p, 'r', encoding='utf-8') as fh:
            return json.load(fh)
    except Exception:
        return None

def compare_reports(before, after):
    b_files = set(before.get('files', {}).keys()) if before else set()
    a_files = set(after.get('files', {}).keys()) if after else set()
    added = sorted(list(a_files - b_files))
    removed = sorted(list(b_files - a_files))
    changed = []
    for f in sorted(a_files & b_files):
        if before['files'].get(f) != after['files'].get(f):
            changed.append(f)
    return {'added': added, 'removed': removed, 'changed': changed}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--report-dir', default='build')
    p.add_argument('--target', help='path to write provided content to (optional)')
    p.add_argument('--content-file', help='file containing content to write to target (optional)')
    p.add_argument('--run-exe', action='store_true', help='run dist\\KickerOS.exe after checks')
    args = p.parse_args()

    report_dir = Path(args.report_dir)
    report_dir.mkdir(parents=True, exist_ok=True)
    before = report_dir / 'preflight_before.json'
    after = report_dir / 'preflight_after.json'

    # run before
    run_preflight(before)
    before_rep = load_report(before)

    backup = None
    if args.target and args.content_file:
        target = Path(args.target)
        content_path = Path(args.content_file)
        if not content_path.exists():
            print('Content file not found:', content_path)
            sys.exit(2)
        # backup
        if target.exists():
            backup = target.with_suffix(target.suffix + '.bak')
            shutil.copy2(target, backup)
            print('Backed up', target, 'to', backup)
        else:
            print('Target does not exist, will create:', target)
        # write content
        shutil.copy2(content_path, target)
        print('Wrote content to', target)

    # run after
    run_preflight(after)
    after_rep = load_report(after)

    diff = compare_reports(before_rep or {}, after_rep or {})
    summary = {
        'before_report': str(before),
        'after_report': str(after),
        'added_files': diff['added'],
        'removed_files': diff['removed'],
        'changed_files': diff['changed']
    }
    summary_path = report_dir / 'shellx_diff_summary.json'
    with open(summary_path, 'w', encoding='utf-8') as fh:
        json.dump(summary, fh, indent=2)
    print('WROTE', summary_path)
    print('Summary:', json.dumps(summary, indent=2))

    # run exe if requested
    if args.run_exe:
        exe = Path('dist') / 'KickerOS.exe'
        if exe.exists():
            logp = report_dir / 'shellx_run.log'
            with open(logp, 'wb') as out:
                print('Running exe:', exe)
                proc = subprocess.Popen([str(exe)], stdout=out, stderr=subprocess.STDOUT)
                proc.wait()
            print('WROTE', logp)
        else:
            print('Exe not found:', exe)

    # restore backup
    if backup and backup.exists():
        shutil.copy2(backup, target)
        backup.unlink()
        print('Restored', target, 'from', backup)

if __name__ == '__main__':
    main()
