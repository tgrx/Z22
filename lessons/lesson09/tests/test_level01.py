from typing import Callable


def verify(module):
    func_name = "compare_triplets"

    assert hasattr(module, func_name)

    compare_triplets = getattr(module, func_name)
    assert isinstance(compare_triplets, Callable)

    assert compare_triplets((1, 0, 1), (0, 1, 0)) == (2, 1)


def test(modules_level01):
    for module in modules_level01.values():
        verify(module)
