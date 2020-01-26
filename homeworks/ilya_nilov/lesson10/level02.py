def plus_minus(coll):
    nmin = 0
    npls = 0
    null = 0
    for elm in coll:
        if elm < 0:
            nmin += 1
        elif elm > 0:
            npls += 1
        else:
            null += 1
    lenght = len(coll)
    return f"{npls/lenght:.6f}\n{nmin/lenght:.6f}\n{null/lenght:.6f}"
