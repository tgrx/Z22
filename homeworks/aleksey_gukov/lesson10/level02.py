def plus_minus(lst):
    pol = otr = nyl = 0
    for arg in lst:
        if arg > 0:
            pol += 1
        if arg < 0:
            otr += 1
        if arg == 0:
            nyl += 1
    dol_pol = pol / len(lst)
    dol_otr = otr / len(lst)
    dol_nyl = nyl / len(lst)
    return f"{dol_pol:.{6}f}\n{dol_otr:.{6}f}\n{dol_nyl:.{6}f}"
