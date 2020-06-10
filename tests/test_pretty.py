from nhttp.server import *


@pretty_handle('/')
def p(w :ResponseWriter, _):
    w.send_response(200)
    w.send_header({'content-type': 'text/plain'})

    return 'Hello Nezha from PrettyFuncHandler'


listen_and_service(':5013')
