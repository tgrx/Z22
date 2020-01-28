from homeworks.aleksey_gukov.lesson11 import level03


class User(level03.User):
    def validate(self):
        if self.name == "" or self.email == "":
            raise ValueError("You should enter your name and email")

        if isinstance(self.name, str) is False and isinstance(self.email, str) is False:
            raise ValueError("You should enter your correct name and email")

        if "@" not in self.email:
            raise ValueError("You miss symbol @ in email")

        for let in self.name:
            if not "a" <= let <= "z" and not "0" <= let <= "9":
                raise ValueError("Your name is incorrect")

        if self.email.count("@") > 1:
            raise ValueError("no @ in host of mail")

        mail_name = self.email.split("@")[0]
        mail_host = self.email.split("@")[1]

        for lett in mail_name:
            if not "a" <= lett <= "z" and not "0" <= lett <= "9":
                raise ValueError("Your name in email is incorrect")

        if mail_name == "" or mail_host == "":
            raise ValueError("You should enter your correct email")

        if not self.name[0].isalpha() or not mail_name[0].isalpha():
            raise ValueError("first symbol in name in email name should be letter")

        if not mail_host[0].isalpha():
            raise ValueError("first symbol in host in email should be letter")
        if mail_host[0] == "." or mail_host[-1] == ".":
            raise ValueError('no first or last symbol "." in host')
