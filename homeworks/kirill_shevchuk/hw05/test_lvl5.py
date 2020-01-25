from homeworks.kirill_shevchuk.hw05.level05 import unique


def test_unique():
    assert unique("123")
    assert not unique((1, 1))
