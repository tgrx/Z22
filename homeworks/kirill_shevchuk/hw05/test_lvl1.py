from homeworks.kirill_shevchuk.hw05.level01 import summa


def test_level1():
    assert summa("", "") == ""
    assert summa("1", "2") == "12"
    assert summa((), ()) == ()
    assert summa((1,), ("a",)) == (1, "a")
    assert summa(1, 2) == 3
    assert summa([1], [2]) == [1, 2]
