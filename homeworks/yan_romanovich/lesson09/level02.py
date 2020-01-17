def rotate_left(lst_01, y):
    for i in range(y):
        lst_01.append(lst_01.pop(0))
        lst_02 = lst_01[:]
    return lst_02
