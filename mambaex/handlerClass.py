from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from .request import Request
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

class ThreadedServerWithAppStack(ThreadedHTTPServer):
    def __init__(self, appstack, hostporttupple, HandlerClass):
        self.appstack = appstack
        ThreadedHTTPServer.__init__(self, hostporttupple, HandlerClass)

class HandlerMambaServer(BaseHTTPRequestHandler):
    def __process_request(self):
        print(dir(self.server.appstack))
        req = Request(self)
    def do_GET(self):
        self.__process_request()
    def do_POST(self):
        self.__process_request()
    def do_DELETE(self):
        self.__process_request()
    def do_PUT(self):
        self.__process_request()
    def do_PATCH(self):
        self.__process_request()
