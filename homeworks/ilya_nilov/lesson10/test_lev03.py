from homeworks.ilya_nilov.lesson10.level03 import validate_password


def test():
    assert validate_password("") == 5
    assert validate_password("aVerySecurePassWord") == 1
    assert validate_password("theSuperVerySecurePassWord") == 0
    assert validate_password("theSuperSuperVerySecurePassWord") == 0
