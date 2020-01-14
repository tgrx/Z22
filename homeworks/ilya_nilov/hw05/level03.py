def good_phone(phnnmbr):
    if not phnnmbr or not phnnmbr[1:].isdigit():
        return False
    key = phnnmbr.startswith("+375", 0, 4) and len(phnnmbr) == 13
    return key
