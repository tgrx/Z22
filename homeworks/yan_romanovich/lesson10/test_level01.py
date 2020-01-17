from homeworks.yan_romanovich.lesson10 import level01


def test():
    assert level01.big_summa(i for i in range(10)) == 45
    assert level01.big_summa((i for i in range(10)), 1) == 46
    assert level01.big_summa(2, (i for i in range(10)), 1) == 48
    assert level01.big_summa({-1, 1, 0}) == 0
