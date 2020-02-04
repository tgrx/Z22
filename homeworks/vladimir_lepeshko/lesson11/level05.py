from homeworks.vladimir_lepeshko.hw05 import level03
from homeworks.vladimir_lepeshko.lesson11 import level04


class User(level04.User):
    def __init__(self, phone, *args, **kwargs):
        level04.User.__init__(self, *args, **kwargs)
        self.phone = phone

    def validate(self):
        level04.User.validate(self)
        if not level03.good_phone(self.phone):
            raise ValueError
