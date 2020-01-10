def compare_triplets(tr1, tr2):
    while i <= tr1:
        if tr1[i] > tr2[i]:
            cntr[0] = +1
        if tr1[i] == tr2[i]:
            cntr[1] = -1
        cntr[1] = +1
        i = +1
    return cntr
