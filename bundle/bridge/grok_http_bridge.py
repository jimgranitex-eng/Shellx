"""Local AI bridge stub.

This minimal bridge listens on /grok?q= and returns simple plain-text replies
so the QML front-end can be tested end-to-end without external APIs.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json
import subprocess
import sys
from pathlib import Path

HOST = "127.0.0.1"
PORT = 8765
PROJECT_ROOT = Path(__file__).resolve().parent.parent

def simple_local_ai(prompt: str) -> str:
    return f"I heard you say: {prompt}\n(This is the local AI stub replying.)"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/grok":
            qs = parse_qs(parsed.query)
            prompt = qs.get("q", [""])[0]

            reply = simple_local_ai(prompt)
            body = reply.encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if parsed.path == "/search":
            qs = parse_qs(parsed.query)
            prompt = qs.get("q", [""])[0]
            try:
                proc = subprocess.run(
                    [sys.executable, str(PROJECT_ROOT / "headless_browser.py"), prompt],
                    cwd=str(PROJECT_ROOT),
                    capture_output=True,
                    text=True,
                    timeout=25,
                )
                payload = json.loads(proc.stdout) if proc.stdout else {"query": prompt, "results": []}
                raw_results = payload.get("results", [])

                listings = []
                for i, item in enumerate(raw_results[:20]):
                    if isinstance(item, dict):
                        listings.append({
                            "id": i,
                            "title": item.get("title", ""),
                            "url": item.get("url", ""),
                            "image": item.get("image", ""),
                            "price": item.get("price", ""),
                            "mileage": item.get("mileage", ""),
                        })
                    else:
                        listings.append({
                            "id": i,
                            "title": str(item),
                            "url": "",
                            "image": "",
                            "price": "",
                            "mileage": "",
                        })

                body = json.dumps({"ok": True, "query": prompt, "listings": listings}).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            except Exception as ex:
                body = json.dumps({"ok": False, "query": prompt, "error": str(ex), "listings": []}).encode("utf-8")
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path != "/evaluate":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")
        try:
            print('[BRIDGE] Received /evaluate body:', body[:1000])
            payload = json.loads(body)
            user_query = payload.get("query", "")
            listings = payload.get("listings", [])
        except Exception as ex:
            print('[BRIDGE] /evaluate parse error:', ex)
            print('[BRIDGE] raw body:', body)
            err_obj = {'ok': False, 'error': 'parse_error', 'exception': str(ex), 'raw_body': body}
            resp = json.dumps(err_obj).encode('utf-8')
            self.send_response(400)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(resp)))
            self.end_headers()
            self.wfile.write(resp)
            return

        # Produce a lightweight fake evaluation for testing
        items = []
        for i, it in enumerate(listings[:20]):
            title = it.get("title") if isinstance(it, dict) else str(it)
            score = max(0, 100 - i*3)
            items.append({
                "id": i,
                "title": title,
                "score": score,
                "summary": f"Auto-eval {i}: matches query '{user_query}' with score {score}.",
                "pros": "Good mileage; clean title",
                "cons": "Needs inspection",
                "url": it.get("url") if isinstance(it, dict) else "",
                "image": it.get("image") if isinstance(it, dict) else ""
            })

        tree = {"topic": user_query, "count": len(items)}
        best_ids = [it["id"] for it in sorted(items, key=lambda x: -x["score"])[:4]]
        resp_obj = {"tree": tree, "items": items, "best_ids": best_ids, "comparison_notes": "Auto-generated comparison."}

        resp = json.dumps(resp_obj).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(resp)))
        self.end_headers()
        self.wfile.write(resp)

def run():
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Local AI bridge running at http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
