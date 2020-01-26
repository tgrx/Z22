def diag_diff(matrix):
    difference = 0
    counter = 0
    for elm in matrix:
        difference += elm[counter]
        difference -= elm[-counter - 1]
        counter += 1
    return abs(difference)
