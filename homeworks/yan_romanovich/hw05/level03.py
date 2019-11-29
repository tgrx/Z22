def good_phone(n):
    if len(n) == 13:
        if nomer[:4:] == "+375":
            return "good_phone"
    else:
        return "not good_phone"
