import string
from homeworks.ilya_nilov.lesson11.level03 import User as User3


def latin_validate(input_name):
    not_cyrillic_letters = string.ascii_letters + string.digits
    for letter in input_name:
        if letter not in not_cyrillic_letters:
            raise ValueError


def not_empty(input_name):
    if not input_name:
        raise ValueError


def name_isalnum_case(input_name):
    case = input_name.islower()
    symbols = input_name.isalnum()
    if not case or not symbols:
        raise ValueError


def is_first_letter(input_name):
    if not input_name[0].isalpha():
        raise ValueError


def email_correct(input_mail_name):
    splittable = "@" in input_mail_name
    if not input_mail_name or splittable:
        raise ValueError


def not_dotted(input_mail_host):
    start = input_mail_host[0] == "."
    end = input_mail_host[-1] == "."
    if start or end:
        raise ValueError


def not_add(input_mail_host, n_add):
    if n_add > 2:
        raise ValueError
    if "@" in input_mail_host:
        raise ValueError


class User(User3):
    def validate(self):
        # """проверка имени"""
        # name_lits = list(str(self.name))
        latin_validate(self.name)
        not_empty(self.name)
        name_isalnum_case(self.name)
        is_first_letter(self.name)

        # """проверка почты"""
        email_lits = self.email.split("@")
        n_adds = len(email_lits)
        # """имя"""
        email_correct(email_lits[0])
        latin_validate(email_lits[0])
        name_isalnum_case(email_lits[0])
        is_first_letter(email_lits[0])

        # """хост"""
        not_empty(email_lits[1])
        is_first_letter(email_lits[1])
        not_dotted(email_lits[1])
        not_add(email_lits[1], n_adds)
