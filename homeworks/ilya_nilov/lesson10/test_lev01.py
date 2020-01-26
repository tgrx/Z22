from homeworks.ilya_nilov.lesson10.level01 import big_summa


def test():
    assert big_summa(1, 2, 3) == 6
    assert big_summa(i for i in range(10)) == 45
