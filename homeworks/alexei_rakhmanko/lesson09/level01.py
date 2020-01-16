"""Уровень 1"""


def compare_triplets(_x, _y):
    """функция сравнения"""
    res1 = 0
    res2 = 0
    for i in range(3):
        if _x[i] > _y[i]:
            res1 += 1
        else:
            res2 += 1
    return res1, res2
