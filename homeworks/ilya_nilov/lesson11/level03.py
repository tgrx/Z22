from homeworks.ilya_nilov.lesson11.level02 import User as User2


class User(User2):
    def __eq__(self, other):
        if isinstance(other, User):
            return self.email == other.email
        return False
