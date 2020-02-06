from datetime import datetime


def make_headers(http_dict):
    headers_str = []
    for key, value in http_dict.items():
        if isinstance(value, int):
            value = str(value)
        if isinstance(value, datetime):
            value = value.strftime("%a, %e %b %Y %H:%M:%S GMT")
        headers_str.append(f"{key}: {value}")
    headers_str = "\n".join(headers_str)
    return headers_str
