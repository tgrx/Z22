def big_summa(*numlist):
    thesum = 0
    for arg in numlist:
        if isinstance(arg, int):
            thesum += arg
        else:
            for slag in arg:
                thesum += slag
    return thesum
