from socketserver import ThreadingMixIn
from http.server import HTTPServer


# old version of python do not have 'ThreadingHTTPServer'
class NHTTPThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True
