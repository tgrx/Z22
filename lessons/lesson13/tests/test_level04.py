# pylint: disable=C0103

_CLASS_NAME = "Response"


def verify_module(module):
    assert hasattr(
        module, _CLASS_NAME
    ), f"module {module.__name__} has no attribute {_CLASS_NAME}"


def verify_class(cls):
    assert isinstance(cls, type), f"{cls} is not a class"
    assert cls.mro() == [cls, object], f"{cls} has unexpected parents"
    assert "__init__" in cls.__dict__, f"{cls} has no constructor (__init__)"
    assert "__str__" in cls.__dict__, f"{cls} has no string-conversion method (__str__)"


def verify_codes(cls):
    assert (
        str(cls(code=200)) == "HTTP/1.1 200 OK\n"
    ), "response does not support popular code 200"
    assert (
        str(cls(code=201)) == "HTTP/1.1 201 Created\n"
    ), "response does not support popular code 201"
    assert (
        str(cls(code=204)) == "HTTP/1.1 204 No Content\n"
    ), "response does not support popular code 204"
    assert (
        str(cls(code=301)) == "HTTP/1.1 301 Moved Permanently\n"
    ), "response does not support popular code 301"
    assert (
        str(cls(code=302)) == "HTTP/1.1 302 Found\n"
    ), "response does not support popular code 302"
    assert (
        str(cls(code=400)) == "HTTP/1.1 400 Bad Request\n"
    ), "response does not support popular code 400"
    assert (
        str(cls(code=401)) == "HTTP/1.1 401 Unauthorized\n"
    ), "response does not support popular code 401"
    assert (
        str(cls(code=403)) == "HTTP/1.1 403 Forbidden\n"
    ), "response does not support popular code 403"
    assert (
        str(cls(code=404)) == "HTTP/1.1 404 Not Found\n"
    ), "response does not support popular code 404"
    assert (
        str(cls(code=405)) == "HTTP/1.1 405 Method Not Allowed\n"
    ), "response does not support popular code 405"
    assert (
        str(cls(code=500)) == "HTTP/1.1 500 Internal Server Error\n"
    ), "response does not support popular code 500"


def verify(module):
    verify_module(module)

    Response = getattr(module, _CLASS_NAME)
    verify_class(Response)
    verify_codes(Response)

    resp = Response(body="a" * 10)
    assert (
        str(resp) == "HTTP/1.1 200 OK\n\naaaaaaaaaa"
    ), "response does not support body serializing"

    resp = Response(body="a" * 10, headers={"Content-Length": 10})
    assert (
        str(resp) == "HTTP/1.1 200 OK\nContent-Length: 10\n\naaaaaaaaaa"
    ), "response does not support body & headers serializing"


def test(modules_level04):
    for module in modules_level04.values():
        verify(module)
