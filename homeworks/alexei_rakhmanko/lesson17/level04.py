"""Уровень 4"""


def my_filter(func, k):
    """Функция"""
    res = []
    for i in k:
        if func(i):
            res.append(i)
    return res
