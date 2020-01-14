from typing import Callable


def verify(module):
    func_name = "diag_diff"

    assert hasattr(module, func_name)

    diag_diff = getattr(module, func_name)
    assert isinstance(diag_diff, Callable)

    assert diag_diff([[1]]) == 0
    assert diag_diff([[1, 0], [0, 1]]) == 2
    assert diag_diff([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 0


def test(modules_level04):
    for module in modules_level04.values():
        verify(module)
