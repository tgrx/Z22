def big_summa(*args):
    return sum(big_summa(*a) if hasattr(a, "__iter__") else a for a in args)
