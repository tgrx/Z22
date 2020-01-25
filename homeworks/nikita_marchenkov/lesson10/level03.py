import re


def validate_password(line):
    result = len(re.findall("[A-Z]", line))
    if result < 5:
        return 5 - result
    return 0
