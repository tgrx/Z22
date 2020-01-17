def big_summa(*args):
    summa = 0
    for i in args:
        if isinstance(i, int):
            summa += i
        else:
            for j in i:
                summa += j
    return summa
