import time
from pathlib import Path

def run_worker(mode):
    time.sleep(0.12)
    return f"Worker {mode} completed"

def generate_report(results):
    return "\n".join([f"Step: {r['step']}\nResult: {r['result']}\n" for r in results])

def main():
    seq = 'Superman → AutoFix → Debug → Deep → Checklist --report'
    cleaned = seq.replace('--report', '').strip()
    steps = [s.strip() for s in cleaned.split('→')] if '→' in cleaned else [cleaned]
    results = []
    for step in steps:
        result = run_worker(step)
        results.append({'step': step, 'result': result})
    report = generate_report(results)
    # Print the report to stdout so it appears on-screen instead of being written to a file
    print(report)

if __name__ == '__main__':
    main()
