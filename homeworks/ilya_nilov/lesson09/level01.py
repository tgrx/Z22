def compare_triplets(tr1, tr2):
    pnt1 = 0
    pnt2 = 0
    for i in (i for i, j in zip(tr1, tr2) if i > j):
        pnt1 = pnt1 + 1
    for i in (i for i, j in zip(tr1, tr2) if j > i):
        pnt2 = pnt2 + 1
    return (pnt1, pnt2)
