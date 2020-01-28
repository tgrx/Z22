from homeworks.nikita_marchenkov.hw05.level03 import good_phone
from homeworks.nikita_marchenkov.lesson11 import level04_failure


class User(level04_failure.User):
    def __init__(self, name, email, phone):
        level04_failure.User.__init__(self, name, email)
        self.phone = phone

    def validate(self):
        level04_failure.User.validate(self)
        if not good_phone(self.phone):
            raise ValueError("Check the phone number!!!")
