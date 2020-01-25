import re

WORD_RE = re.compile("[A-Z][a-z]+")


def validate_password(password: str) -> int:
    words = len(WORD_RE.findall(password))
    return 5 - words if words < 5 else 0
