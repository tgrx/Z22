from homeworks.aleksey_gukov.lesson09 import level01


def test():
    assert level01.compare_triplets((1, 0, 1), (0, 1, 0)) == (2, 1)
