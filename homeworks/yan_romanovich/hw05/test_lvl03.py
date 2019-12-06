from homeworks.yan_romanovich.hw05 import level03


def test_good_phone():
    assert level03.good_phone("+375172294660")
    assert level03.good_phone("+375296648778")
    assert not level03.good_phone("")
    assert not level03.good_phone("+37517229466")
    assert not level03.good_phone("+37517229466a")
    assert not level03.good_phone("+791562655123")
    assert not level03.good_phone("+3751722946601")
    assert not level03.good_phone("2020327")
    assert not level03.good_phone(None)
