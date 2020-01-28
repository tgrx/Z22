from homeworks.yan_romanovich.hw05 import level03
from homeworks.yan_romanovich.lesson11 import level04_failure


class User(level04_failure.User):
    def __init__(self, name, email, phone):
        level04_failure.User.__init__(self, name, email)
        self.phone = phone

    def validate(self):
        level04_failure.User.validate(self)
        if not level03.good_phone(self.phone):
            raise ValueError
