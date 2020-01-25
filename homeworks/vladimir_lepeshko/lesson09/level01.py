def compare_triplets(arg1, arg2):
    points = [0, 0]
    for digit in range(3):
        if arg1[digit] > arg2[digit]:
            points[0] += 1
        if arg1[digit] < arg2[digit]:
            points[1] += 1
    return tuple(points)
