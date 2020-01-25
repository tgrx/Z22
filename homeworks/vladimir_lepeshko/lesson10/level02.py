def plus_minus(coll_int):
    plus = minus = zero = 0
    base = 1
    per_base = base / len(coll_int)

    for value in coll_int:
        if value > 0:
            plus += 1
            per_plus = plus * per_base

        if value < 0:
            minus += 1
            per_minus = minus * per_base

        if value == 0:
            zero += 1
            per_zero = zero * per_base

    return f"{per_plus:.{6}f}\n{per_minus:.{6}f}\n{per_zero:.{6}f}"
