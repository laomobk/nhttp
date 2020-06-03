from http.server import BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def send_header(self, keyword :str, value :str):
        print(f'[TEST] send_header({keyword}, {value})')

    def send_error(self, code :int, message :str='', explain :str=''):
        print(f'[TEST] send_error({keyword}, {value})')

    def send_response(self, code :int, message :str=''):
        print(f'[TEST] send_response({code}, {message})')
