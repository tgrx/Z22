from random import randint


def key(_arg):
    """
    Returns a random integer in [0, 2**64)
    Outgoing correlation between original and sorted < 1%

    Also have tried:
    * `hash(arg)`   17% correlation
    * `id(arg)`     98% correlation
    """
    return randint(0, 2 ** 64 - 1)
