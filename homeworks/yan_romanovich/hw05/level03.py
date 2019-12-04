def good_phone(nomer):
    return nomer is not None and len(nomer) == 13 and "+375" in nomer and nomer[1:].isdigit()
