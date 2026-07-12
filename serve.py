from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os

os.chdir('/root/nihon-offshore')

class Handler(SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass  # quiet: don't spam tracebacks on client resets

if __name__ == '__main__':
    ThreadingHTTPServer(('0.0.0.0', 8090), Handler).serve_forever()
