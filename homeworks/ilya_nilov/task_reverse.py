def listrev(incmng_list):
    assert isinstance(incmng_list, list)
    list_lenhgt = len(incmng_list)
    outcmng_list = incmng_list[:]
    lim = 0
    while (lim) != list_lenhgt:
        lim = lim + 1
        outcmng_list[lim - 1] = incmng_list[-lim]
    return outcmng_list


# L1 = [1, 2, 3]
# print(L1)

# L2 = listrev(L1)
# print(L1)
# print(L2)
