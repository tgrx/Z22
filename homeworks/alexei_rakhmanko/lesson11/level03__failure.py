"""уровень 3"""
# pylint: disable=R0903
from homeworks.alexei_rakhmanko.lesson11 import level02


class User(level02.User):
    """класс"""

    def __eq__(self, other):
        if isinstance(self, User):
            return self.email == other.email
        return False
