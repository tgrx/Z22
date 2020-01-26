from homeworks.ilya_nilov.lesson10.level04 import diag_diff


def test():
    assert diag_diff([[1]]) == 0
    assert diag_diff([[1, 0], [0, 1]]) == 2
    assert diag_diff([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 0
