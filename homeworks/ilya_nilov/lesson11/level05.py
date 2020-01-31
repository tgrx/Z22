from homeworks.ilya_nilov.lesson11.level04 import User as User4
from homeworks.ilya_nilov.hw05.level03 import good_phone


class User(User4):
    def __init__(self, phone, *args, **kwargs):
        User4.__init__(self, *args, **kwargs)
        self.phone = phone

    def validate(self):
        try:
            User4.validate(self)
        except ValueError:
            raise ValueError("Ошибка данных юзера")
        if not good_phone(self.phone):
            raise ValueError("Ошибка данных телефона")
