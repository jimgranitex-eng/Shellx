import subprocess
import json
import sys

query = sys.argv[1]

proc = subprocess.run(
    ["python", "headless_browser.py", query],
    capture_output=True,
    text=True
)

print(proc.stdout)
