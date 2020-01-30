from homeworks.kirill_shevchuk.lesson11 import level03


class User(level03.User):
    def validate(self):
        validate_name(self.name)
        validate_email(self.email)
        email_name = self.email.split("@")[0]
        email_adres = self.email.split("@")[1]
        validate_name(email_name)
        validate_email_adres(email_adres)


def validate_name(name):
    if not name:
        raise ValueError
    if not isinstance(name, str):
        raise ValueError
    if name[0].isdigit():
        raise ValueError
    if not set(name).issubset("abcdefghijklmnopqrstuvwxyz" + "1234567890"):
        raise ValueError


def validate_email(email):
    if not email:
        raise ValueError
    if not isinstance(email, str):
        raise ValueError
    if email.count("@") > 1 and len(email) > 2:
        raise ValueError


def validate_email_adres(email_adres):
    if not email_adres:
        raise ValueError
    if not isinstance(email_adres, str):
        raise ValueError
    if email_adres[0].isdigit():
        raise ValueError
    if email_adres[0] == "." or email_adres[-1] == ".":
        raise ValueError
