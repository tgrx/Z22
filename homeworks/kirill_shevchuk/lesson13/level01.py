def get_headers(http_str):
    string = http_str.split("\n")
    kollection = {}
    del string[0], string[string.index("") :]
    for i in string:
        kollection[i.split(": ")[0]] = i.split(": ")[1]
    return kollection
