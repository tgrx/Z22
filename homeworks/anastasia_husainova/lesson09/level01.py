def compare_triplets(t1, t2):
    p1 = 0
    p2 = 0

    for pos in [0, 1, 2]:

        if t1[pos] > t2[pos]:
            p1 += 1
        else:
            if t1[pos] < t2[pos]:
                p2 += 1
            else:
                pass

    return p1, p2