from homeworks.yan_romanovich.hw05.level03 import good_phone


def test_good_phone():
    assert good_phone("+375172294660")
    assert good_phone("+375296648778")
    assert not good_phone("")
    assert not good_phone("+37517229466")
    assert not good_phone("+37517229466a")
    assert not good_phone("+791562655123")
    assert not good_phone("+3751722946601")
    assert not good_phone("2020327")
    assert not good_phone(None)
