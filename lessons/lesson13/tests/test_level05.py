# pylint: disable=C0103

from random import choice
from typing import NoReturn

_CLASS_NAME = "Server"


def verify_module(module):
    assert hasattr(
        module, _CLASS_NAME
    ), f"module {module.__name__} has no attribute {_CLASS_NAME}"


def verify_class(cls):
    assert isinstance(cls, type), f"{cls} is not a class"
    assert cls.mro() == [cls, object], f"{cls} has unexpected parents"
    assert "__init__" in cls.__dict__, f"{cls} has no constructor (__init__)"
    assert "add_handler" in cls.__dict__, f"{cls} has no method add_handler"
    assert "serve" in cls.__dict__, f"{cls} has no method serve"

    assert "Redirect" in cls.__dict__, f"{cls} has no internal class Redirect"
    Redirect = getattr(cls, "Redirect")
    assert isinstance(Redirect, type), f"{cls}.Redirect is not a class"
    assert issubclass(
        Redirect, Exception
    ), f"{cls}.Redirect does not subclass the Exception"


def handler_index(server, url) -> str:
    assert server, "server has not been passed to the handler"
    assert url, "url has not been passed to the handler"
    return f"Hi there!"


def handler_200(server, url) -> str:
    assert server, "server has not been passed to the handler"
    assert url, "url has not been passed to the handler"
    return f"scheme={url.scheme}"


def handler_302(server, url) -> NoReturn:
    assert server, "server has not been passed to the handler"
    assert url, "url has not been passed to the handler"
    raise server.Redirect


def handler_500(server, url) -> NoReturn:
    assert server, "server has not been passed to the handler"
    assert url, "url has not been passed to the handler"

    exceptions = (
        Exception,
        NameError,
        RuntimeError,
        TypeError,
        ValueError,
        ZeroDivisionError,
    )

    raise choice(exceptions)("kek")


def verify(module):
    verify_module(module)

    Server = getattr(module, _CLASS_NAME)
    verify_class(Server)

    server = Server("my")
    server.add_handler("", handler_index)
    server.add_handler("/scheme", handler_200)
    server.add_handler("/redirect", handler_302)
    server.add_handler("/xxx", handler_500)

    assert server.serve("http://my") == "HTTP/1.1 200 OK\n\nHi there!"
    assert server.serve("http://my/") == "HTTP/1.1 200 OK\n\nHi there!"
    assert server.serve("my/redirect") == "HTTP/1.1 302 Found\n"
    assert server.serve("my/xxx") == "HTTP/1.1 500 Internal Server Error\n\nkek"
    assert server.serve("mz/xxx") == "HTTP/1.1 404 Not Found\n"
    assert server.serve("my/yyy") == "HTTP/1.1 404 Not Found\n"
    assert (
        server.serve("postgresql://my/scheme") == "HTTP/1.1 200 OK\n\nscheme=postgresql"
    )


def test(modules_level05):
    for module in modules_level05.values():
        verify(module)
