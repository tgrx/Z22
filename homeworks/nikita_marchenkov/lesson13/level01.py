def get_headers(text):
    list_a = text.split("\n")[1:]
    list_headers = []

    for i in list_a:
        if not i:
            break
        list_headers.append(i.split(": "))

    return dict(list_headers)
