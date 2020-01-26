def diag_diff(arr):
    len_col = len(arr)
    sum_diag1 = sum_diag2 = 0
    for row in enumerate(arr):
        for col in enumerate(arr):
            sum_diag1 += arr[row[0]][row[0]]
            sum_diag2 += arr[row[0]][len_col - col[0] - 1]
    return sum_diag1 - sum_diag2
