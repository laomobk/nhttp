import requests

from nhttp.server import *


@handle('/query')
def h_normal(w :ResponseWriter, req :Request):
    w.send_response(200)

    print(req.query_dict)


def test_query():
    requests.get('localhost:5013/query?a=10&b=10')


listen_and_service(':5013')

test_query()
