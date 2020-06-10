from nhttp.server.lovely import Response, LovelyFuncHandler
from nhttp.server import *


def f(_):
    return Response(200, None, 
            '<h1>Hello Nezha from lovely function handler</h1>')


set_handler('/', LovelyFuncHandler(f))

listen_and_service(':5013')
