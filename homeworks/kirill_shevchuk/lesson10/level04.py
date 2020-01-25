def diag_diff(array):
    sum1 = sum2 = 0
    if len(array) is not len(array[0]):
        return False
    for ipos in enumerate(array):
        for jpos in enumerate(array):
            sum1 += array[ipos[0]][ipos[0]]
            sum2 += array[ipos[0]][len(array) - 1 - jpos[0]]
    return sum1 - sum2
