from homeworks.yan_romanovich.hw05 import level03


def test():
    assert level03.good_phone("+375172294660")
    assert level03.good_phone("+375296648778")
    assert not level03.good_phone("+791562655123")
    assert not level03.good_phone("2020327")
