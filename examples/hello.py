from nhttp.server import *
from nhttp.server.handler import HelloWorldHandler


set_handler('/', HelloWorldHandler())

listen_and_service(':5013')
