from typing import Callable


def verify(module):
    func_name = "host"
    assert hasattr(module, func_name)

    host = getattr(module, func_name)
    assert isinstance(host, Callable)

    assert host("") == ""
    assert host("/a/b") == ""
    assert host("/a/b") == ""
    assert host("gist.github.com") == "gist.github.com"
    assert host("git@github.com:tgrx/Z22.git") == "github.com"
    assert host("https://github.com/tgrx/Z22/") == "github.com"
    assert host("test.com/a/b/c") == "test.com"
    assert host(None) == ""


def test(modules_level04):
    for module in modules_level04.values():
        verify(module)
