from . import level04
from ..hw05.level03 import good_phone


class User(level04.User):
    def __init__(self, phone, *args, **kw):
        super().__init__(*args, **kw)
        self.phone = phone

    def validate(self):
        super().validate()
        validate_phone(self.phone)


def validate_phone(phone: str):
    if not isinstance(phone, str):
        raise ValueError("phone is not a string")

    if not good_phone(phone):
        raise ValueError("phone is malformed")
