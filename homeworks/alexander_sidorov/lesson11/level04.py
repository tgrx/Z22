from . import level03


class User(level03.User):
    def validate(self):
        validate_name(self.name)
        validate_email(self.email)


def validate_name(name: str):
    verify_name_is_nonempty(name)
    verify_name_is_alnum(name)
    verify_name_startswith_letter(name)


def validate_email(email):
    verify_email_is_nonempty(email)
    validate_email_consistence(email)


def verify_name_is_nonempty(name: str):
    if not name:
        raise ValueError("name is empty")


def verify_name_is_alnum(name):
    if not isinstance(name, str):
        raise ValueError(f"name `{name!r}` is not a string")
    if not name.isalnum():
        raise ValueError(f"name `{name!r}` has non-alphanumeric chars")


def verify_name_startswith_letter(name):
    if not name[0].islower():
        raise ValueError(f"name `{name!r}` does not start with lowercase letter")


def verify_email_is_nonempty(email):
    if not email:
        raise ValueError("email is empty")


def validate_email_consistence(email):
    verify_email_is_string(email)
    validate_email_parts(email)


def verify_email_is_string(email):
    if not isinstance(email, str):
        raise ValueError(f"email `{email!r}` is not a string")


def validate_email_parts(email):
    parts = email.split("@")
    if len(parts) != 2:
        raise ValueError(f"email `{email!r}` is malformed")

    name, host = parts

    validate_name(name)
    validate_host(host)


def validate_host(host: str):
    if not isinstance(host, str):
        raise ValueError("host is not a string")

    if not host:
        raise ValueError("host is empty")

    if not host[0].islower():
        raise ValueError("host does not start with a lowercase letter")

    if host[0] == ".":
        raise ValueError("host starts with a dot")

    if host[-1] == ".":
        raise ValueError("host ends with a dot")

    if "@" in host:
        raise ValueError("host contains an '@' char")
