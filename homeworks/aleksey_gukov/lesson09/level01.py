def compare_triplets(tup_first, tup_second):
    f_res = 0
    s_res = 0
    if len(tup_first) == len(tup_second) == 3:
        for i in range(3):
            if tup_first[i] > tup_second[i]:
                f_res += 1
            if tup_first[i] < tup_second[i]:
                s_res += 1
    return (f_res, s_res)
