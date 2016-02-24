import os
import BaseHTTPServer
import CGIHTTPServer


class PyHTTPRequestHandler(CGIHTTPServer.CGIHTTPRequestHandler):
    def do_POST(self):
        if self.is_cgi():
            CGIHTTPServer.CGIHTTPRequestHandler.do_POST(self)
        else:
            self.do_GET()

    def is_python(self, path):
        head, tail = os.path.splitext(path)
        return tail.lower() in (".py", ".pyw", ".cgi")

host = ''
port = 8000
BaseHTTPServer.HTTPServer(
    (host, port),
    PyHTTPRequestHandler
    ).serve_forever()
