# pylint: disable=C0103
from random import choice
from typing import NoReturn

_CLASS_NAME = "Server"


def verify_module(module):
    assert hasattr(module, _CLASS_NAME)


def verify_class(cls):
    assert isinstance(cls, type)
    assert cls.mro() == [cls, object]
    assert "__init__" in cls.__dict__
    assert "add_handler" in cls.__dict__
    assert "serve" in cls.__dict__

    assert "Redirect" in cls.__dict__
    Redirect = getattr(cls, "Redirect")
    assert isinstance(Redirect, type)
    assert issubclass(Redirect, Exception)


def handler_index(server, url) -> str:
    assert server
    assert url
    return f"Hi there!"


def handler_200(server, url) -> str:
    assert server
    return f"scheme={url.scheme}"


def handler_302(server, url) -> NoReturn:
    assert url
    raise server.Redirect


def handler_500(server, url) -> NoReturn:
    assert server
    assert url
    raise choice(
        (Exception, NameError, RuntimeError, TypeError, ValueError, ZeroDivisionError,)
    )("kek")


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
