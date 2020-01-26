from homeworks.yan_romanovich.lesson11 import level04
from homeworks.yan_romanovich.hw05 import level03


class User(level04.User):
    def __init__(self, name, email, phone):
        level04.User.__init__(self, name, email)
        self.phone = phone

    def validate(self):
        level04.User.validate(self)
        if not level03.good_phone(self.phone):
            raise ValueError
