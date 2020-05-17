from nhttp.server import *


_html_source = '''
<h1> Hello Nezha from NHTTP </h1>
</br>
<h2> URI: {uri} </h2>
<h2> Method: {method} </h2>
<h2> Headers: </h2>
{headers}
<hr/>
<h1> content </h1>
{content}
'''


@handle('/')
def say_hello(w :ResponseWriter, r :Request):
    w.send_respone(200)
    w.send_header({'Content-type': 'text/html'})

    w.write(_html_source.format(

        uri=r.uri,
        method=r.method,
        headers=''.join(['<h3>%s : %s</h3>' % (k, v) 
                for k, v in r.headers.items()]),
        content=r.raw_content

        ))

listen_and_service(':5013')


