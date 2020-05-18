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

            chset = self.headers.get_charset()
            cont_type = self.headers.get_content_type()

            if chset is not None:
                self.__content_charset = chset

            if cont_type is not None:
                self.__content_type = cont_type

            self.__raw_content = self.__base_handler.rfile.read(length).decode(self.__content_charset)

        except (KeyError, TypeError):
            # TODO log.
            pass
