import re

from homeworks.nikita_marchenkov.lesson11 import level03


def check(text, error):
    if not text:
        raise ValueError(error)


def instance(text, error):
    if not isinstance(text, str):
        raise ValueError(error)


def latin_numbers(text, error):
    if not re.match(r"^[a-z0-9]+$", text):
        raise ValueError(error)


def first_symbol(text, error):
    if not text[0].isalpha():
        raise ValueError(error)


class User(level03.User):
    def validate(self):
        check(self.name, "Write your name!")
        check(self.email, "Write your email!")
        instance(self.name, "You should enter correct name!")
        instance(self.email, "You should enter correct email!")
        latin_numbers(
            self.name, "You should use only small latin letters or numbers in name!"
        )
        first_symbol(self.name, "First symbol in name should be a letter!")

        list_email = re.split("@", self.email)
        if len(list_email) > 2:
            raise ValueError("Email has more than one @.")
        email_name = list_email[0]
        email_host = list_email[1]
        check(email_name, "Write name in email!")
        check(email_host, "Write host in email!")
        latin_numbers(
            email_name,
            "You should use small latin letters or numbers in name of email!",
        )
        first_symbol(email_name, "First symbol in name of email should be a letter!")
        first_symbol(email_host, "First symbol in host of email should be a letter!")
        if email_host[0] == "." or email_host[-1] == ".":
            raise ValueError("Host can not start or end with '.'")
