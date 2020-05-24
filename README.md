# NHTTP
A simple and friendly HTTP library

## install

```sh
python setup.py install
```

## hello world

```python
from nhttp.server import *
from nhttp.server.handler import HelloWorldHandler


set_handler('/', HelloWorldHandler)
listen__and_serve(':5013')
```

```sh
$ curl 127.0.0.1:5013
Hello World!
```
