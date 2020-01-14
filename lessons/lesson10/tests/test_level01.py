from typing import Callable


def verify(module):
    func_name = "big_summa"

    assert hasattr(module, func_name)

    big_summa = getattr(module, func_name)
    assert isinstance(big_summa, Callable)

    assert big_summa(i for i in range(10)) == 45
    assert big_summa((i for i in range(10)), 1) == 46
    assert big_summa(2, (i for i in range(10)), 1) == 48
    assert big_summa({-1, 1, 0}) == 0


def test(modules_level01):
    for module in modules_level01.values():
        verify(module)
