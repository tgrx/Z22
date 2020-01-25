from typing import Callable


def verify(module):
    func_name = "plus_minus"

    assert hasattr(module, func_name)

    plus_minus = getattr(module, func_name)
    assert isinstance(plus_minus, Callable)

    assert plus_minus((1, 1, 0, -1, -1)) == "0.400000\n0.400000\n0.200000"


def test(modules_level02):
    for module in modules_level02.values():
        verify(module)
