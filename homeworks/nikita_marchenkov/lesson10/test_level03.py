from homeworks.nikita_marchenkov.lesson10 import level03


def test():
    assert level03.validate_password("") == 5
    assert level03.validate_password("aVerySecurePassWord") == 1
    assert level03.validate_password("theSuperVerySecurePassWord") == 0
    assert level03.validate_password("theSuperSuperVerySecurePassWord") == 0
