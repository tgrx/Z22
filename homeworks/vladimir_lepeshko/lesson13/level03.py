from datetime import datetime


def make_headers(http_headers_dict):
    headers_info_list = []
    for key, value in http_headers_dict.items():
        if isinstance(value, int):
            value = str(value)
        if isinstance(value, datetime):
            value = value.strftime("%a, %e %b %Y %H:%M:%S GMT")
        info = f"{key}: {value}"
        headers_info_list.append(info)
    headers_info = "\n".join(headers_info_list)
    return headers_info
