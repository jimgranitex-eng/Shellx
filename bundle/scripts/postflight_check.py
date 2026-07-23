#!/usr/bin/env python3
"""Postflight wrapper: runs preflight_check and compares before/after snapshots."""
import subprocess
import os
import sys
import json
from datetime import datetime

ROOT = os.getcwd()
PRE = os.path.join(ROOT,'build','preflight_before.json')
POST = os.path.join(ROOT,'build','preflight_after.json')

def run_preflight(outfile):
    cmd = [sys.executable, os.path.join('scripts','preflight_check.py'), '--report', outfile]
    print('Running:', ' '.join(cmd))
    subprocess.check_call(cmd)

def diff(a,b):
    with open(a,'r',encoding='utf-8') as fa, open(b,'r',encoding='utf-8') as fb:
        ra=json.load(fa); rb=json.load(fb)
    da=set(ra['files'].keys()); db=set(rb['files'].keys())
    added = sorted(list(db-da))
    removed = sorted(list(da-db))
    return {'added':added,'removed':removed}

def main():
    run_preflight(PRE)
    input('Apply your change now and press Enter to continue...')
    run_preflight(POST)
    d = diff(PRE,POST)
    report = {'timestamp': datetime.utcnow().isoformat()+'Z', 'diff': d}
    outf = os.path.join('build','postflight_diff.json')
    with open(outf,'w',encoding='utf-8') as fh:
        json.dump(report, fh, indent=2)
    print('WROTE', outf)

if __name__=='__main__':
    main()
