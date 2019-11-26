from homeworks.ilya_nilov import task_reverse


def test():
    assert task_reverse.listrev([1, 2, 3, 4]) == [4, 3, 2, 1]
