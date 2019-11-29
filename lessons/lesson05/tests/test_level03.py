from typing import Callable


def verify(module):
    func_name = "good_phone"
    assert hasattr(module, func_name)

    good_phone = getattr(module, func_name)
    assert isinstance(good_phone, Callable)

    assert good_phone("+375172294660")
    assert good_phone("+375296648778")
    assert not good_phone("")
    assert not good_phone("+37517229466")
    assert not good_phone("+37517229466a")
    assert not good_phone("+791562655123")
    assert not good_phone("+3751722946601")
    assert not good_phone("2020327")
    assert not good_phone(None)


def test(modules_level03):
    for module in modules_level03.values():
        verify(module)
