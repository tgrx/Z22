def good_phone(nomer):
    if nomer is not None:
        if len(nomer) == 13 and "+375" in nomer and nomer[1:].isdigit():
            return True
        return False
    return False
