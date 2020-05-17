from http.server import BaseHTTPRequestHandler


class Request:
    def __init__(self, handler :BaseHTTPRequestHandler, method :str):
        self.__base_handler = handler
        self.__method = method

        self.__content = {}
        self.__raw_content = ''
        self.__content_type = ''
        self.__content_charset = 'UTF-8'

        self.read_content()

    @property
    def content(self):
        return self.__content

    @property
    def raw_content(self):
        return self.__raw_content

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

    @property
    def request_file(self):
        return self.__base_handler.rfile

    @property
    def _base_handler(self):
        return self.__base_handler

    def __parse_content_info(self, info :str):
        info = info.replace(' ', '')
        cont_type, *extra = info.split(';')

    def read_content(self):
        try:

            length = int(self.__base_handler.headers['Content-Length'])
            cont_type_and_chset = self.__base_handler.headers['Content-Type']

             

            self.__raw_content = self.__base_handler.rfile.read(length)

        except KeyError:
            # TODO log.
            pass
