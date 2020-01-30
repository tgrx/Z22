from homeworks.kirill_shevchuk.lesson11 import level04
from homeworks.kirill_shevchuk.hw05.level03 import good_phone


class User(level04.User):
    def __init__(self, phone, *args, **kwargs):
        self.phone = phone
        level04.User.__init__(self, *args, **kwargs)

    def validate(self):
        level04.User.validate(self)
        if not good_phone(self.phone):
            raise ValueError
