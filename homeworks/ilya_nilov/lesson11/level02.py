from homeworks.ilya_nilov.lesson11.level01 import User as User1


class User(User1):
    def __init__(self, name, email):
        self.name = name
        self.email = email
