def diag_diff(massiv):
    summa1 = summa2 = 0
    for i in range(len(massiv)):
        summa1 += massiv[i][i]
        summa2 += massiv[i][len(massiv) - i - 1]
    return summa1 - summa2
