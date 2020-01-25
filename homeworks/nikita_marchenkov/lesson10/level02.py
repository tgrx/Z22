def plus_minus(listing):
    pos = 0
    neg = 0
    zer = 0
    for i in listing:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        elif i == 0:
            zer += 1
    div_pos = pos / len(listing)
    div_neg = neg / len(listing)
    div_zer = zer / len(listing)
    return f"{div_pos:.6f}\n{div_neg:.6f}\n{div_zer:.6f}"
