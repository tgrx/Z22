from homeworks.nikita_marchenkov.lesson11 import level04
from homeworks.nikita_marchenkov.hw05.level03 import good_phone


class User(level04.User):
    def __init__(self, name, email, phone):
        level04.User.__init__(self, name, email)
        self.phone = phone

    def validate(self):
        level04.User.validate(self)
        if not good_phone(self.phone):
            raise ValueError("Check the phone number!!!")
