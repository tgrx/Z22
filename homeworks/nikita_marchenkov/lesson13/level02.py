from datetime import datetime
from homeworks.nikita_marchenkov.lesson13.level01 import get_headers


def get_typed_headers(text):
    new_dictionary = get_headers(text)

    if "Date" in new_dictionary:
        right_date_format = datetime.strptime(
            new_dictionary["Date"], "%a, %d %b %Y %H:%M:%S %Z"
        )
        new_dictionary["Date"] = right_date_format
    if "Content-Length" in new_dictionary:
        right_content_format = new_dictionary["Content-Length"]
        new_dictionary["Content-Length"] = int(right_content_format)

    return new_dictionary
