def diag_diff(matriza):
    first_diag = second_diag = 0
    razmer = len(matriza)
    for i in range(razmer):
        first_diag += matriza[i][i]
        second_diag += matriza[i][razmer - i - 1]
    return first_diag - second_diag
