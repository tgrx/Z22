from homeworks.yan_romanovich.lesson10 import level04


def test():
    assert level04.diag_diff([[1]]) == 0
    assert level04.diag_diff([[1, 0], [0, 1]]) == 2
    assert level04.diag_diff([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 0
