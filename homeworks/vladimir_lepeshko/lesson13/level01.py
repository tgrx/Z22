def get_headers(http_data):
    if not isinstance(http_data, str):
        raise ValueError
    http_data_in_list = []
    http_data = http_data.split("\n")
    http_data.remove(http_data[0])
    del http_data[http_data.index("") :]
    for data in http_data:
        http_data_in_list.append(data.split(": "))
    return dict(http_data_in_list)
