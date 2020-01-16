def compare_triplets(first, second):
    result_1 = 0
    result_2 = 0
    for i in range(3):
        if first[i] > second[i]:
            result_1 += 1
        elif first[i] < second[i]:
            result_2 += 1
    return (result_1, result_2)
