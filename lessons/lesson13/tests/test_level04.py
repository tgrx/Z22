# pylint: disable=C0103

_CLASS_NAME = "Response"


def verify_module(module):
    assert hasattr(module, _CLASS_NAME)


def verify_class(cls):
    assert isinstance(cls, type)
    assert cls.mro() == [cls, object]
    assert "__init__" in cls.__dict__
    assert "__str__" in cls.__dict__


def verify_codes(cls):
    assert str(cls(code=200)) == "HTTP/1.1 200 OK\n"
    assert str(cls(code=201)) == "HTTP/1.1 201 Created\n"
    assert str(cls(code=204)) == "HTTP/1.1 204 No Content\n"
    assert str(cls(code=301)) == "HTTP/1.1 301 Moved Permanently\n"
    assert str(cls(code=302)) == "HTTP/1.1 302 Found\n"
    assert str(cls(code=400)) == "HTTP/1.1 400 Bad Request\n"
    assert str(cls(code=401)) == "HTTP/1.1 401 Unauthorized\n"
    assert str(cls(code=403)) == "HTTP/1.1 403 Forbidden\n"
    assert str(cls(code=404)) == "HTTP/1.1 404 Not Found\n"
    assert str(cls(code=405)) == "HTTP/1.1 405 Method Not Allowed\n"
    assert str(cls(code=500)) == "HTTP/1.1 500 Internal Server Error\n"


def verify(module):
    verify_module(module)

    Response = getattr(module, _CLASS_NAME)
    verify_class(Response)
    verify_codes(Response)

    resp = Response(body="a" * 10)
    assert str(resp) == "HTTP/1.1 200 OK\n\naaaaaaaaaa"

    resp = Response(body="a" * 10, headers={"Content-Length": 10})
    assert str(resp) == "HTTP/1.1 200 OK\nContent-Length: 10\n\naaaaaaaaaa"


def test(modules_level04):
    for module in modules_level04.values():
        verify(module)
