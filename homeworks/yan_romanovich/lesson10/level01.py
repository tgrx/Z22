def big_summa(*args):
    result = 0
    for nomer in args:
        if isinstance(nomer, int):
            result += nomer
        else:
            for quality in nomer:
                result += quality
    return result
