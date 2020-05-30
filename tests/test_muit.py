from nhttp.server import *


@handle('/')
def r(w :ResponseWriter, _):
    w.send_respone(200)
    w.send_header({'content-type':'text/html'})
    w.write('/')

    print('/')


@handle('/a/')
def rr(w, _):
    w.send_respone(200)
    w.send_header({'content-type':'text/html'})
    w.write('/a')

    print('/a')


@handle('/a/b')
def rrr(w, _):
    w.send_respone(200)
    w.send_header({'content-type':'text/html'})
    w.write('/a/b')

    print('/a/b')


listen_and_service(':5013')
