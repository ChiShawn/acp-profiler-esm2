#!/usr/bin/env python3
"""Minimal portfolio web demo for ACP-Profiler.

This is not the production research webapp. It is a lightweight demonstration
showing the intended user interaction: submit a peptide sequence and receive a
context-aware IC50 profiling placeholder.
"""

from __future__ import annotations

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse


HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>ACP-Profiler Portfolio Demo</title>
  <style>
    body { font-family: system-ui, sans-serif; margin: 2rem; max-width: 760px; }
    input { width: 100%; padding: 0.7rem; font-family: monospace; }
    button { margin-top: 0.8rem; padding: 0.6rem 1rem; }
    .box { margin-top: 1.2rem; padding: 1rem; border: 1px solid #ddd; border-radius: 8px; }
  </style>
</head>
<body>
  <h1>ACP-Profiler</h1>
  <p>Portfolio demo for context-aware anticancer peptide IC50 profiling.</p>
  <form>
    <label>Peptide sequence</label>
    <input name="sequence" value="{sequence}" placeholder="Example: FLFKLIPKAIKGLIKAFK">
    <button type="submit">Profile</button>
  </form>
  {result}
</body>
</html>
"""


def normalize_sequence(value: str) -> str:
    return "".join(ch for ch in value.upper() if ch.isalpha())


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        query = parse_qs(urlparse(self.path).query)
        sequence = normalize_sequence(query.get("sequence", [""])[0])
        result = ""
        if sequence:
            result = (
                "<div class='box'>"
                f"<strong>Input length:</strong> {len(sequence)} aa<br>"
                "<strong>Output:</strong> production model returns ranked IC50 profiles "
                "across supported experimental contexts."
                "</div>"
            )
        payload = HTML.format(sequence=sequence, result=result).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


def main() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", 7860), Handler)
    print("Serving portfolio demo on http://127.0.0.1:7860")
    server.serve_forever()


if __name__ == "__main__":
    main()
