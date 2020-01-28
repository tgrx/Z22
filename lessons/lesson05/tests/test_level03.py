from typing import Callable

BAD_PHONES = {
    "",
    "+37517229466",
    "+37517229466a",
    "+791562655123",
    "+3751722946601",
    "2020327",
    None,
}


def verify(module):
    func_name = "good_phone"
    assert hasattr(module, func_name)

    good_phone = getattr(module, func_name)
    assert isinstance(good_phone, Callable)

    assert good_phone("+375172294660")
    assert good_phone("+375296648778")

    for bad_phone in BAD_PHONES:
        assert not good_phone(bad_phone)


def test(modules_level03):
    for module in modules_level03.values():
        verify(module)
