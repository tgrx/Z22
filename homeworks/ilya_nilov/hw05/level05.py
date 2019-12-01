def unique(collect):
    
    
    if not collect:
        return False
    setarr = set(collect)
    if len(collect) == len(setarr):
        return True
    return False

