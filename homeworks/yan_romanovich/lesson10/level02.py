def plus_minus(koll):
    plus = null = minus = 0
    for i in koll:
        if i > 0:
            plus += 1
        elif i == 0:
            null += 1
        else:
            minus += 1
    leng = len(koll)
    res1 = plus / leng
    res2 = minus / leng
    res3 = null / leng
    return f"{res1:.6f}\n{res2:.6f}\n{res3:.6f}"
