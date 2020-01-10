def rotate_left(lits, nrot):
    cplits = lits[nrot:]
    cplits.extend(lits[:nrot])
    return cplits