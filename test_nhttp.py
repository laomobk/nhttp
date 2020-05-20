from nhttp.server import *
import time


_html_source = '''
<h1> Hello Nezha from NHTTP </h1>
</br>
<h2> URL: {url} </h2>
<h2> Query: {query} </h2>
<h2> Method: {method} </h2>
<h2> Headers: </h2>
{headers}
<br/>
<h1> Content </h1>
{content}
'''


@handle('/')
def say_hello(w :ResponseWriter, r :Request):
    w.send_respone(200)
    w.send_header({'Content-type': 'text/html'})

    w.write(_html_source.format(

        url=r.url,
        query=str(r.query_dict),
        method=r.method,
        headers=''.join(['<h3>%s : %s</h3>' % (k, v) 
                for k, v in r.headers.items()]),
        content=str(r.raw_content)

        ))


@handle('/red/')
def handle_redirect(w :ResponseWriter, _):
    w.send_respone(301)
    w.send_header({'location': '/'})


@handle('/host')
def handle_host(w :ResponseWriter, r :Request):
    w.send_respone(200)
    w.send_header({'Content-type': 'text/html'})
    w.write('here is /host')


@handle('/host/')
def handle_host(w :ResponseWriter, r :Request):
    w.send_respone(200)
    w.send_header({'Content-type': 'text/html'})
    w.write('here is /host/')


@handle('/a/')
def handle_host(w :ResponseWriter, r :Request):
    w.send_respone(200)
    w.send_header({'Content-type': 'text/html'})
    w.write('here is a')


listen_and_service(':5013')


