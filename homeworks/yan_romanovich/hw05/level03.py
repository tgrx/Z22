def good_phone(nomer):
    if len(nomer) == 13 and nomer[:4:] == "+375":
        return "good_phone"
    return "not good_phone"
