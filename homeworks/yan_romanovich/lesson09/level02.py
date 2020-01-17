def rotate_left(lst_01, raz):
    lst_02 = lst_01[:]
    for _i in range(raz):
        lst_02.append(lst_02.pop(0))
    return lst_02
