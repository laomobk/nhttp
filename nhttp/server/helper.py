from os.path import getsize

from .lovely import LovelyPlugin, Response
from ..constant.content_type_table import CONTENT_TYPE_DICT


def iter_file(f, chunk_size=-1) -> bytes:
    while True:
        b = f.read(chunk_size)
    
        if not b:
            break

        yield b
