from typing import Callable


def verify(module):
    func_name = "hello"

    assert hasattr(module, func_name)

    hello = getattr(module, func_name)
    assert isinstance(hello, Callable)

    assert hello("") == "Hi!"
    assert hello("Alex") == "Hello, Alex!"
    assert hello(None) == "Hi!"


def test(modules_level02):
    for module in modules_level02.values():
        verify(module)
