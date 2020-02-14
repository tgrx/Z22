from project.consts import COINAGE


COINAGE = list(reversed(list(COINAGE.items())))


def get_change(money):
    money *= 100
    result = {}
    for i in COINAGE:
        if money < i[1]:
            pass
        elif money >= i[1]:
            result[i[0]] = 0
            while money >= i[1]:
                money -= i[1]
                result[i[0]] += 1
    return result
