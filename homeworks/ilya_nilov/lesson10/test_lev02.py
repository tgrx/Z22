from homeworks.ilya_nilov.lesson10.level02 import plus_minus


def test():
    assert (
        plus_minus([1, 1, 0, -1, -1])
        == """0.400000
0.400000
0.200000"""
    )
