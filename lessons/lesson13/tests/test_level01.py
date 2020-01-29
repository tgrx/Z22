from typing import Callable


def verify(module, response):
    func_name = "get_headers"
    assert hasattr(
        module, func_name
    ), f"module {module.__name__} has no attribute {func_name}"

    get_headers = getattr(module, func_name)
    assert isinstance(
        get_headers, Callable
    ), f"entity {module.__name__}.{func_name} is not a function"

    headers = get_headers(response)

    assert isinstance(headers, dict), f"function result is not a dict"
    assert len(headers) == 8, f"mismatch in amount of headers returned"

    assert headers == {
        "Connection": "keep-alive",
        "Content-Length": "4053",
        "Content-Type": "text/html; charset=utf-8",
        "Date": "Sun, 26 Jan 2020 14:07:02 GMT",
        "Server": "gunicorn/19.9.0",
        "Vary": "Cookie",
        "Via": "1.1 vegur",
        "X-Frame-Options": "SAMEORIGIN",
    }, "mismatch in headers keys and values"


def test(modules_level01, benzak_http_response):
    for module in modules_level01.values():
        verify(module, benzak_http_response)
