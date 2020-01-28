import re

from homeworks.nikita_marchenkov.lesson11 import level03


class User(level03.User):
    def validate(self):
        if isinstance(self.name, str) is False and isinstance(self.email, str) is False:
            raise ValueError("You should enter your correct name and email")
        if self.name == "" or self.email == "":
            raise ValueError("Write your name or email!")
        for letter in self.name:
            if letter != letter.lower():
                raise ValueError("Use in name only low case!")
            if not self.name[0].isalpha():
                raise ValueError("First symbol in name should be letter!")
        if self.email != re.findall(r"\w+@\w+.\w+", self.email)[0]:
            email_name = re.split("@", self.email)[0]
            email_email = re.split("@", self.email)[1]
            if email_name == "":
                raise ValueError("Write your name in email!")
            for letter in email_name:
                if letter != letter.lower():
                    raise ValueError("Use in name only low case!")
                if not email_name[0].isalpha():
                    raise ValueError("First symbol in name should be letter!")
            if not email_email[0].isalpha():
                raise ValueError("First symbol in mail should be letter!")
            raise ValueError(
                "Your email must contain 'name', @, 'host' and 'domain', for example 'alex@mail.ru'"
            )
