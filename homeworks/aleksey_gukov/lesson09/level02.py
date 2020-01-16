def rotate_left(list_f, step):
    for _ in range(step):
        list_f.append(list_f.pop(0))
        list_s = list_f[:]
    return list_s
