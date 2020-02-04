import re
from homeworks.vladimir_lepeshko.lesson11 import level03


class User(level03.User):
    def validate(self):
        if not (isinstance(self.name, str) and isinstance(self.email, str)):
            raise ValueError

        def verify_validate_invalid_name():
            if not self.name:
                raise ValueError
            if self.name[0].isdigit():
                raise ValueError
            if not self.name.islower():
                raise ValueError
            if not self.name.isalnum():
                raise ValueError
            if not re.search(r"[a-zA-Z0-9]", self.name):
                raise ValueError

        def verify_validate_invalid_email_name():
            email_name = self.email.split("@")[0]
            if email_name[0].isdigit():
                raise ValueError
            if not email_name:
                raise ValueError
            if not email_name.islower():
                raise ValueError
            if not email_name.isalnum():
                raise ValueError
            if not re.search(r"[a-zA-Z0-9]", email_name):
                raise ValueError

        def verify_validate_invalid_email_host():
            email_host = self.email.split("@")[1]
            if not email_host:
                raise ValueError
            if email_host.startswith("."):
                raise ValueError
            if email_host.endswith("."):
                raise ValueError
            if email_host[0].isdigit():
                raise ValueError
            if self.email.count("@") > 1:
                raise ValueError

        def verify_validate_invalid_email():
            if not self.email:
                raise ValueError
            email_host = self.email.split("@")[1]
            email_name = self.email.split("@")[0]
            if not self.email:
                raise ValueError
            if not email_host:
                raise ValueError
            if not email_name:
                raise ValueError

        verify_validate_invalid_name()
        verify_validate_invalid_email()
        verify_validate_invalid_email_name()
        verify_validate_invalid_email_host()
