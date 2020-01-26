from homeworks.nikita_marchenkov.lesson11 import level02


class User(level02.User):
    def __eq__(self, other):
        if isinstance(other, User):
            return self.email == other.email
        return NotImplemented
