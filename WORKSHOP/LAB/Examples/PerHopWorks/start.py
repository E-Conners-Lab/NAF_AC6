#!/usr/bin/env python3
"""Run Per-Hop Works with Python alone, from any working directory."""
import argparse
import functools
import http.server
from pathlib import Path
import threading
import webbrowser

ROOT = Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8000)
    parser.add_argument('--no-browser', action='store_true')
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error('port must be between 1 and 65535')
    if not (ROOT / 'index.html').exists():
        parser.exit(1, 'The game entry point has not been built yet. See implementation-status.json.\n')
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
    try:
        server = http.server.ThreadingHTTPServer(('127.0.0.1', args.port), handler)
    except OSError as error:
        parser.exit(1, f'Could not start port {args.port}: {error}. Try --port 8001.\n')
    url = f'http://localhost:{args.port}'
    print(f'Per-Hop Works: {url}\nPress Ctrl+C to stop.', flush=True)
    if not args.no_browser:
        def open_browser():
            try:
                if not webbrowser.open(url):
                    print(f'Open {url} in your browser to begin.', flush=True)
            except webbrowser.Error:
                print(f'Open {url} in your browser to begin.', flush=True)
        threading.Timer(0.3, open_browser).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nFactory stopped.')
    finally:
        server.server_close()

if __name__ == '__main__':
    main()
