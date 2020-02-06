from datetime import datetime
from homeworks.kirill_shevchuk.lesson13.level01 import get_headers


def get_typed_headers(http_str):
    dictionary = get_headers(http_str)
    for key, value in dictionary.items():
        if value.isdigit():
            dictionary[key] = int(value)
        if key == "Date":
            dictionary[key] = datetime.strptime(value, "%a, %d %b %Y %H:%M:%S %Z")
    return dictionary
