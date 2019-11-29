from homeworks.ilya_nilov.hw05.level03 import good_phone


def test():
    assert good_phone("+375172294660") == True
    assert good_phone("+375296648778") == True
    assert good_phone("+791562655123") == False
    assert good_phone("2020327") == False