#!/usr/bin/env python3
"""Browser runner for QProcess integration.

Direct-execution script that accepts a query as command-line argument,
performs search/AI operations, and outputs JSON to stdout for QML consumption.

Usage:
    python browser_runner.py "your search query here"

Output format (JSON):
{
    "reply": "AI response text",
    "answer": "AI response text (alias)",
    "results": [...],
    "query": "original query",
    "timestamp": "ISO timestamp"
}
"""
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parent

def simple_local_ai(prompt: str) -> str:
    """Minimal AI stub - replace with actual Grok/LLM API call if available."""
    return f"I heard you say: {prompt}\n(This is the local AI stub replying via QProcess.)"

def run_browser_search(query: str) -> list:
    """Run headless browser search via subprocess."""
    try:
        proc = subprocess.run(
            [sys.executable, str(PROJECT_ROOT / "headless_browser.py"), query],
            cwd=str(PROJECT_ROOT),
            capture_output=True,
            text=True,
            timeout=25,
        )
        payload = json.loads(proc.stdout) if proc.stdout else {"results": []}
        return payload.get("results", [])
    except Exception as ex:
        print(json.dumps({"error": f"Browser search failed: {ex}", "results": []}), file=sys.stderr)
        return []

def main():
    if len(sys.argv) < 2:
        output = {
            "error": "No query provided",
            "reply": "Error: No query argument",
            "answer": "Error: No query argument",
            "query": "",
            "results": [],
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        print(json.dumps(output))
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    
    # Get AI response
    ai_reply = simple_local_ai(query)
    
    # Optionally run browser search (can be disabled for faster response)
    search_results = run_browser_search(query) if query else []
    
    # Format output for QML consumption
    output = {
        "reply": ai_reply,
        "answer": ai_reply,  # alias for compatibility
        "query": query,
        "results": search_results[:20],  # limit to 20 results
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "status": "ok"
    }
    
    # Output JSON to stdout (QML will parse this)
    print(json.dumps(output, indent=2))
    sys.exit(0)

if __name__ == "__main__":
    main()
