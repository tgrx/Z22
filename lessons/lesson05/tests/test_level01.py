from typing import Callable


def verify(module):
    func_name = "summa"

    assert hasattr(module, func_name)

    summa = getattr(module, func_name)
    assert isinstance(summa, Callable)

    assert summa("", "") == ""
    assert summa("1", "2") == "12"
    assert summa((), ()) == ()
    assert summa((1,), ("a",)) == (1, "a")
    assert summa(1, 2) == 3
    assert summa([1], [2]) == [1, 2]


def test(modules_level01):
    for module in modules_level01.values():
        verify(module)
