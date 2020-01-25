from . import level02


class User(level02.User):
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False

        return self.email == other.email
