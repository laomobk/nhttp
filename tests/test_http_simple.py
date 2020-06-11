from nhttp.server import *

@handle('/')
def handle_root(w :ResponseWriter, _):
    w.send_respone(200)
    w.send_header({'content-type': 'text/html'})
    w.write('Hello Nezha')


listen_and_service(':5013', True)
