def good_phone(phnnmbr):
    assert isinstance(phnnmbr, str)
    pref = "+375"
    if phnnmbr[0:4] == pref and len(phnnmbr) == 13:
        for elm in phnnmbr[1:]:
            if not elm.isdigit():
                return False
        return True
    else:
        return False
