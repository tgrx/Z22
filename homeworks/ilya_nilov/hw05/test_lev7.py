from homeworks.ilya_nilov.hw05.level07 import enqueue
from homeworks.ilya_nilov.hw05.level07 import dequeue


def test():

    x = {}
    assert dequeue(x) is None
    assert dequeue(x, 1, "a") is None
    assert dequeue(x, 1, "b") is None
    assert dequeue(x, 2, "aa") is None
    assert dequeue(x) == "aa"
    assert dequeue(x, 1, "c") is None
    assert dequeue(x, 3, "aaa") is None
    assert dequeue(x, 3, "bbb") is None
    assert dequeue(x, 2, "bb") is None
    assert dequeue(x) == "aaa"
    assert dequeue(x) == "bbb"
    assert dequeue(x) == "bb"
    assert dequeue(x) == "a"
    assert dequeue(x) == "b"
    assert dequeue(x) == "c"
    assert dequeue(x) is None
    assert x == {}
