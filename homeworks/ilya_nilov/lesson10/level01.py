def big_summa(*args):
    summ = 0
    for elm in args:
        if isinstance(elm, (int, float)):
            summ += elm
        else:
            for particle in elm:
                summ += particle
    return summ
