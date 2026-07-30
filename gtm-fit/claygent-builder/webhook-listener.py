#!/usr/bin/env python3
"""Minimal webhook listener for Clay callback results."""

import json
import os
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ.get("CLAY_LISTENER_PORT", 8765))
RESULTS_DIR = "./clay-results"

os.makedirs(RESULTS_DIR, exist_ok=True)


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length)) if length else {}
        ts = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        path = os.path.join(RESULTS_DIR, f"{ts}.json")
        with open(path, "w") as f:
            json.dump(body, f, indent=2)
        print(f"[clay-listener] Saved result -> {path}")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"status": "received"}).encode())

    def log_message(self, format, *args):
        pass  # suppress default access logs


if __name__ == "__main__":
    print(f"[clay-listener] Listening on port {PORT}...")
    HTTPServer(("", PORT), Handler).serve_forever()
