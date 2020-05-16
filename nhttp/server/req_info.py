from http.server import BaseHTTPRequestHandler


class Request:
    def __init__(self, handler :BaseHTTPRequestHandler, method :str):
        self.__base_handler = handler
        self.__method = method

    @property
    def client_address(self):
        return self.__base_handler.client_address

    @property
    def method(self):
        return self.__method

    @property
    def uri(self):
        return self.__base_handler.path

    @property
    def headers(self):
        return self.__base_handler.headers

