from datetime import datetime


def make_headers(headers_dict):
    local_dict = datetime_cheker(headers_dict)
    elm = 0
    headers_keys = []
    while elm < len(list(local_dict.items())):
        headers_keys.append(headers_build(list(local_dict.items()), elm))
        elm += 1
    return "\n".join(sorted(headers_keys))


def datetime_cheker(headers_dict):
    new_dict = headers_dict.copy()
    for keys in new_dict:
        if isinstance(new_dict[keys], datetime):
            new_dict[keys] = new_dict[keys].strftime("%a, %e %b %Y %H:%M:%S %zGMT")
    return new_dict


def headers_build(collection, iteration):
    headers_keys = str(collection[iteration][0])
    headers_values = str(collection[iteration][1])
    return headers_keys + ": " + headers_values
