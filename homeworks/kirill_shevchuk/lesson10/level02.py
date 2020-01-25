def plus_minus(kollection):
    minus = plus = null = 0
    for i in kollection:
        if i < 0:
            minus += 1
        elif i > 0:
            plus += 1
        else:
            null += 1
    minus /= len(kollection)
    plus /= len(kollection)
    null /= len(kollection)
    return f"{minus:.{6}f}\n{plus:.{6}f}\n{null:.{6}f}"
