from datetime import datetime
from typing import Callable


def verify(module):
    func_name = "make_headers"
    assert hasattr(
        module, func_name
    ), f"module {module.__name__} has no attribute {func_name}"

    make_headers = getattr(module, func_name)
    assert isinstance(
        make_headers, Callable
    ), f"entity {module.__name__}.{func_name} is not a function"

    headers_dict = {
        "Connection": "keep-alive",
        "Content-Length": 4053,
        "Date": datetime(year=2020, month=1, day=1, hour=1, minute=1, second=1),
    }

    headers_got = make_headers(headers_dict)

    headers_expected = "\n".join(
        (
            "Connection: keep-alive",
            "Content-Length: 4053",
            "Date: Wed,  1 Jan 2020 01:01:01 GMT",
        )
    )

    assert headers_got == headers_expected


def test(modules_level03):
    for module in modules_level03.values():
        verify(module)
