from homeworks.nikita_marchenkov.hw05 import level05


def test():
    assert level05.unique("123")
    assert not level05.unique((1, 1))
