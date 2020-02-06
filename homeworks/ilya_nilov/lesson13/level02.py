from datetime import datetime
from homeworks.ilya_nilov.lesson13.level01 import get_headers


def get_typed_headers(http_answer):
    parsed_dict = get_headers(http_answer)
    for key in parsed_dict:
        if "Length" in key:
            parsed_dict[key] = int(parsed_dict[key])
        elif "Date" in key:
            parsed_dict[key] = datetime.strptime(
                parsed_dict[key], "%a, %d %b %Y %H:%M:%S %Z"
            )
    return parsed_dict
