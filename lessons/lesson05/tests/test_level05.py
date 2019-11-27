from typing import Callable


def verify(module):
    func_name = "unique"
    assert hasattr(module, func_name)

    unique = getattr(module, func_name)
    assert isinstance(unique, Callable)

    assert unique("123")
    assert not unique((1, 1))


def test(modules_level05):
    for module in modules_level05.values():
        verify(module)
