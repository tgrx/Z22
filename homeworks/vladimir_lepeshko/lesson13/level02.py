from datetime import datetime
from homeworks.vladimir_lepeshko.lesson13 import level01


def get_typed_headers(http_response):
    http_data_dict_view = level01.get_headers(http_response)
    for key, value in http_data_dict_view.items():
        if http_data_dict_view[key].isdigit():
            http_data_dict_view[key] = int(value)
        if key == "Date":
            http_data_dict_view["Date"] = datetime.strptime(
                http_data_dict_view["Date"], "%a, %d %b %Y %H:%M:%S %Z"
            )
    return http_data_dict_view
