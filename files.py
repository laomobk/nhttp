import os.path

from nhttp.server.handler import FileServerHandler
from nhttp.server import *

set_handler('/', FileServerHandler('/', '.'))


listen_and_service(':5013')
