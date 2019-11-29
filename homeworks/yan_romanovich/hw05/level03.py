def good_phone(nomer):
    if len(nomer) == 13 and nomer[:4:] == "+375":
        return True
    return False
