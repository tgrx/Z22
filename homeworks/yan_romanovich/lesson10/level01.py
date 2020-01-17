def big_summa(*args):
    result = 0
    for n in args:
        if isinstance(n, int):
            result += n
        else:
            for q in n:
                result += q
    return result
