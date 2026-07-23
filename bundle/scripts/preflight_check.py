#!/usr/bin/env python3
"""Preflight QML environment scanner

Quick checks:
- locate qml and dist/qml folders
- list QML files
- detect duplicates (same basename in multiple folders)
- scan for View3D, SceneEnvironment, Model, PerspectiveCamera, anchors.fill full-screen Rectangles
- basic bracket balance check for QML files
- emit JSON report to stdout or to --report
"""
import os
import re
import json
import argparse

ROOT = os.getcwd()

def find_qml_dirs():
    candidates = [os.path.join(ROOT,'qml'), os.path.join(ROOT,'dist','qml'), os.path.join(ROOT,'build','qml')]
    return [p for p in candidates if os.path.isdir(p)]

def list_qml_files(root):
    files = []
    for dirpath,_,filenames in os.walk(root):
        for f in filenames:
            if f.endswith('.qml'):
                files.append(os.path.join(dirpath,f))
    return files

def read_text(path):
    try:
        with open(path,'r',encoding='utf-8') as fh:
            return fh.read()
    except Exception as e:
        return ''

def simple_checks(path, text):
    checks = {}
    checks['has_View3D'] = bool(re.search(r"\bView3D\b", text))
    checks['has_SceneEnvironment'] = bool(re.search(r"\bSceneEnvironment\b", text))
    checks['has_Model'] = bool(re.search(r"\bModel\b", text))
    checks['has_PerspectiveCamera'] = bool(re.search(r"\bPerspectiveCamera\b", text))
    checks['has_anchors_fill'] = bool(re.search(r"anchors\.fill\s*:\s*parent", text))
    checks['has_fullscreen_rectangle'] = bool(re.search(r"Rectangle\s*\{[^}]*anchors\.fill\s*:\s*parent", text, re.S))
    # bracket balance
    checks['paren_balance'] = text.count('(') - text.count(')')
    checks['brace_balance'] = text.count('{') - text.count('}')
    checks['bracket_balance'] = text.count('[') - text.count(']')
    return checks

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', help='write JSON report to file')
    args = parser.parse_args()

    dirs = find_qml_dirs()
    report = {'root': ROOT, 'qml_dirs': dirs, 'files': {}, 'duplicates': {}, 'summary':{}}

    basename_map = {}
    for d in dirs:
        files = list_qml_files(d)
        for f in files:
            text = read_text(f)
            checks = simple_checks(f, text)
            report['files'][os.path.relpath(f, ROOT)] = checks
            b = os.path.basename(f)
            basename_map.setdefault(b, []).append(os.path.relpath(f, ROOT))

    # duplicates
    for name, paths in basename_map.items():
        if len(paths) > 1:
            report['duplicates'][name] = paths

    # quick summary
    totals = {'files_scanned': len(report['files']), 'qml_dirs': len(dirs), 'duplicate_files': len(report['duplicates'])}
    report['summary'] = totals

    out = json.dumps(report, indent=2)
    if args.report:
        with open(args.report,'w',encoding='utf-8') as fh:
            fh.write(out)
        print('WROTE', args.report)
    else:
        print(out)

if __name__=='__main__':
    main()
