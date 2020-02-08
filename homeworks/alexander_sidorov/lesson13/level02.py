from datetime import datetime
from functools import partial
from typing import Any
from typing import Dict

from .level01 import get_headers

CONVERTERS = {
    "Content-Length": int,
    "Date": lambda _v: datetime.strptime(_v, "%a, %d %b %Y %H:%M:%S GMT"),
}


def convert(converters, header, raw, default=lambda _a: _a):
    converter = converters.get(header, default)
    return converter(raw)


def get_typed_headers(response: str) -> Dict[str, Any]:
    headers = get_headers(response)
    conv = partial(convert, CONVERTERS)

    result = {header: conv(header, value) for header, value in headers.items()}

    return result
