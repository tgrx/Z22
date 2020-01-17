def big_summa(*nums):
    summa = 0
    for i in nums:
        if isinstance(i, int):
            summa += i
        else:
            for j in i:
                summa += j
    return summa
