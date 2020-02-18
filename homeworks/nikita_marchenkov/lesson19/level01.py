from project.consts import COINAGE

COINAGE_LIST = sorted(COINAGE.items(), key=lambda x: x[1], reverse=True)


def get_change(value):

    value = value * 100
    result = {}
    for i in COINAGE_LIST:
        nom = i[1]
        count = value // nom
        if count:
            value = value % nom
            key = list(COINAGE.keys())[list(COINAGE.values()).index(nom)]
            result[key] = int(count)
    return result
