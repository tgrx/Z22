from typing import Callable


def verify(module):
    func_name = "validate_password"

    assert hasattr(module, func_name)

    validate_password = getattr(module, func_name)
    assert isinstance(validate_password, Callable)

    assert validate_password("") == 5
    assert validate_password("aVerySecurePassWord") == 1
    assert validate_password("theSuperSuperVerySecurePassWord") == 0
    assert validate_password("theSuperVerySecurePassWord") == 0


def test(modules_level03):
    for module in modules_level03.values():
        verify(module)
