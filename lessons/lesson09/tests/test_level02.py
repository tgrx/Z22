from typing import Callable


def verify(module):
    func_name = "rotate_left"

    assert hasattr(module, func_name)

    rotate_left = getattr(module, func_name)
    assert isinstance(rotate_left, Callable)

    lst0 = lst1 = [1, 2, 3, 4, 5]
    assert rotate_left(lst0, 2) == [3, 4, 5, 1, 2]
    assert lst0 is lst1


def test(modules_level02):
    for module in modules_level02.values():
        verify(module)
