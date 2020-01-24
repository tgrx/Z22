from homeworks.vladimir_lepeshko.hw05.level03 import good_phone


def test_good_phone():
    assert good_phone("+375172294660")
    assert good_phone("+375296648778")
    assert not good_phone("+791562655123")
    assert not good_phone("2020327")
