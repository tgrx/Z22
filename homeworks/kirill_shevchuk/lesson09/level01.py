def compare_triplets(arg1, arg2):
    score = [0, 0]
    for i in range(3):
        if arg1[i] > arg2[i]:
            score[0] += 1
        else:
            score[1] += 1
    return tuple(score)


assert compare_triplets((1, 0, 1), (0, 1, 0)) == (2, 1)
