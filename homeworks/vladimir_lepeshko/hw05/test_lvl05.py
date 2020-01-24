from homeworks.vladimir_lepeshko.hw05.level05 import unique


def test():
    assert unique("123")
    assert not unique((1, 1))
