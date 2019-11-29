"""тест"""
from homeworks.alexei_rakhmanko import ex


def test_rev():
    """функция теста"""
    assert ex.my_per([1, 2, 3]) == [3, 2, 1]
