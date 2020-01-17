def compare_triplets(pervii, vtoroi):
    point1 = 0
    point2 = 0
    for i in range(3):
        if pervii[i] != vtoroi[i]:
            if pervii[i] > vtoroi[i]:
                point1 += 1
            else:
                point2 += 1
    return (point1, point2)
