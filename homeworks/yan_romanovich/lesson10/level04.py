def diag_diff(massiv):
    summa1 = summa2 = 0
    for i_pos in enumerate(massiv):
        for j_pos in enumerate(massiv):
            summa1 += massiv[i_pos[0]][i_pos[0]]
            summa2 += massiv[i_pos[0]][len(massiv) - 1 - j_pos[0]]
    return summa1 - summa2
