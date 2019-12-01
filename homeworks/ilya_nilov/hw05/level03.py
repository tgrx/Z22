def good_phone(phnnmbr):
    pref = "+375"
    if phnnmbr[0:4] == pref and len(phnnmbr) == 13:
        for elm in phnnmbr[1:]:
            if not elm.isdigit():
                return false
        return True
    else:
        return False
