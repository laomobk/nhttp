from .req_info import Request
from .resp_writer import ResponseWriter


class Handler:
    def serve_http(self, response_writer :ResponseWriter, request :Request):
        pass


class FuncHandler(Handler):
    def __init__(self, handle_func):
        self.__handle_func = handle_func

    def serve_http(self, response_writer :ResponseWriter, request :Request):
        return self.__handle_func(response_writer, request)


class RedirectHandler(Handler):
    def __init__(self, location :str):
        self.__location = location

    def serve_http(self, w :ResponseWriter, r :Request):
        w.send_respone(301)
        w.send_header({'location': self.__location})

 
