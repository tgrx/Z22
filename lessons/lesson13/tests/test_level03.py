from datetime import datetime
from typing import Callable


def verify(module):
    func_name = "make_headers"

    assert hasattr(module, func_name)

    make_headers = getattr(module, func_name)
    assert isinstance(make_headers, Callable)

    headers_dict = {
        "Connection": "keep-alive",
        "Content-Length": 4053,
        "Date": datetime(year=2020, month=1, day=1, hour=1, minute=1, second=1),
    }

    headers = make_headers(headers_dict)

    assert headers == "\n".join(
        (
            "Connection: keep-alive",
            "Content-Length: 4053",
            "Date: Wed,  1 Jan 2020 01:01:01 GMT",
        )
    )


def test(modules_level03):
    for module in modules_level03.values():
        verify(module)
