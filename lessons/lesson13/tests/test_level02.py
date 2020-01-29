from datetime import datetime
from typing import Callable


def verify_on_dataset(func, dataset, expected):
    got = func(dataset)

    assert isinstance(got, dict)
    assert len(got) == len(expected)
    assert got == expected


def verify(module, response):
    func_name = "get_typed_headers"
    assert hasattr(
        module, func_name
    ), f"module {module.__name__} has no attribute {func_name}"

    get_typed_headers = getattr(module, func_name)
    assert isinstance(
        get_typed_headers, Callable
    ), f"entity {module.__name__}.{func_name} is not a function"

    verify_on_dataset(
        get_typed_headers,
        response,
        {
            "Connection": "keep-alive",
            "Content-Length": 4053,
            "Content-Type": "text/html; charset=utf-8",
            "Date": datetime(year=2020, month=1, day=26, hour=14, minute=7, second=2),
            "Server": "gunicorn/19.9.0",
            "Vary": "Cookie",
            "Via": "1.1 vegur",
            "X-Frame-Options": "SAMEORIGIN",
        },
    )

    verify_on_dataset(
        get_typed_headers,
        "HTTP/1.1 200 OK\nConnection: keep-alive\n",
        {"Connection": "keep-alive"},
    )


def test(modules_level02, benzak_http_response):
    for module in modules_level02.values():
        verify(module, benzak_http_response)
