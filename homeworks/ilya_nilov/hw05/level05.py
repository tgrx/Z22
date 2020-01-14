def unique(collect):
    if not collect:
        return False
    setarr = set(collect)
    key = len(collect) == len(setarr)
    return key
