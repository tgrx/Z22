def res(lis):
    lenght = len(lis)
    i = 0
    while i < lenght / 2:
        lis[i], lis[lenght - 1 - i] = lis[lenght - 1 - i], lis[i]
        i += 1

    return lis
