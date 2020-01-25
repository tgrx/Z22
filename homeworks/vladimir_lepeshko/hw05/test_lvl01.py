from homeworks.vladimir_lepeshko.hw05.level01 import summa


def test_summa():
    assert summa("", "") == ""
    assert summa("1", "2") == "12"
    assert summa((), ()) == ()
    assert summa(("1",), (2,)) == ("1", 2)
    assert summa(1, 2) == 3
    assert summa([1], [2]) == [1, 2]
