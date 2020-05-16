from http.server import BaseHTTPRequestHandler

from .writer import ResponseWriter
from .req_info import Request


class MuxEntry:
    def __init__(self, pattern :str, handle_func=None):
        self.pattern = pattern
        self.__handler = handle_func

    def serve_http(self, respone_writer :ResponseWriter, request :Request):
        if self.__handler is not None:
            return self.__handler(respone_writer, request)


class ServerMux(BaseHTTPRequestHandler):
    def __init__(self):
        self.__handlers = []

    def set_handle_func(self, pattern :str, handle_func :str):
        m = MuxEntry(pattern, handle_func)
        self.__handlers.append(m)

    def set_handler(self, entry :MuxEntry):
        self.__handler.append(entry)

    def __find_handler(self, pattern :str) -> MuxEntry:
        for e in self.__handlers:
            if e.pattern == pattern:
                return e
        return None

    def __do_request(self, method :str):
        handler = self.__find_handler(self.path)

        if handler is None:
            self.send_error(404)
            return

        respw = ResponseWriter(self)
        req = Request(self, method)

        handler.serve_http(respw, req)

    def do_GET(self):
        self.__do_request('GET')

    def do_POST(self):
        self.__do_request('POST')

    def __call__(self, *req_info):
        super().__init__(*req_info)
