"""уровень 2"""
# pylint: disable=R0903
from homeworks.alexei_rakhmanko.lesson11 import level01


class User(level01.User):
    """класс"""

    def __init__(self, name, email):
        self.name = name
        self.email = email
