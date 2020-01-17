def diag_diff(matr):
    sum1 = 0
    sum2 = 0
    length = len(matr[0])
    for i in range(length):
        for j in range(length):
            if i == j:
                sum1 = sum1 + matr[i][j]
            if i == length - j - 1:
                sum2 = sum2 + matr[i][j]
    return sum1 - sum2
