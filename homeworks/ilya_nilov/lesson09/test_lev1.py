from homeworks.ilya_nilov.lesson09.level01 import compare_triplets


def test():
    assert compare_triplets((1, 0, 1), (0, 1, 0)) == (2, 1)
