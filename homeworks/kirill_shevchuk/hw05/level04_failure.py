def splitt(string):
    lst = []
    counter = 0
    lenght = len(string)
    for i in range(lenght):
        if string[i] == "/" or string[i] == ":" or string[i] == "@":
            lst.append(string[counter:i])
            counter = i + 1
    return lst


def host(string):
    if string is None:
        return ""
    stroka = splitt(string)
    lenght = len(stroka)
    for i in range(lenght):
        if "." in stroka[i]:
            return stroka[i]
    return ""
