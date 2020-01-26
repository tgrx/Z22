from datetime import datetime
from typing import Callable


def verify(module, response):
    func_name = "get_typed_headers"

    assert hasattr(module, func_name)

    get_typed_headers = getattr(module, func_name)
    assert isinstance(get_typed_headers, Callable)

    headers = get_typed_headers(response)

    assert isinstance(headers, dict)
    assert len(headers) == 8

    assert headers == {
        "Connection": "keep-alive",
        "Content-Length": 4053,
        "Content-Type": "text/html; charset=utf-8",
        "Date": datetime(year=2020, month=1, day=26, hour=14, minute=7, second=2),
        "Server": "gunicorn/19.9.0",
        "Vary": "Cookie",
        "Via": "1.1 vegur",
        "X-Frame-Options": "SAMEORIGIN",
    }


def test(modules_level02, benzak_http_response):
    for module in modules_level02.values():
        verify(module, benzak_http_response)
