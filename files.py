import os.path

from nhttp.server import *

_page = '''
<h1> dictionary of {path} </h1>
<hr/>
{files}
'''


@handle('/')
def list_files(w :ResponseWriter, r :Request):
    d = os.listdir('.')

    w.send_respone(200)
    w.send_header({'Content-type':'text/html'})

    buf = ''

    for f in d:
        buf += '<p> %s </p>' % f

    w.write(_page.format(path=os.path.abspath('.'),
                         files=buf))


listen_and_service(':5013')
