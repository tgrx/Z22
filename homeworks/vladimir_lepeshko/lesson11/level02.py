from homeworks.vladimir_lepeshko.lesson11 import level01


class User(level01.User):
    def __init__(self, name, email):
        self.name = name
        self.email = email
