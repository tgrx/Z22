from homeworks.ilya_nilov.hw05.level05 import unique


def test():
    assert unique("123")
    assert not unique((1, 1))