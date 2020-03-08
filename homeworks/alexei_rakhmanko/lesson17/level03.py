"""Уровень 3"""


def my_map(func, k):
    """Функция"""
    res = []
    for i in k:
        res.append(func(i))
    return res
