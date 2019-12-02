from homeworks.ilya_nilov.hw05.level06 import enqueue
from homeworks.ilya_nilov.hw05.level06 import dequeue


def test():
    q = []

    assert enqueue(q, 100) is None
    assert enqueue(q, 200) is None
    assert len(q) == 2

    assert dequeue(q) == 100
    assert len(q) == 1

    assert enqueue(q, 300) is None
    assert len(q) == 2

    assert dequeue(q) == 200
    assert dequeue(q) == 300
    assert len(q) == 0

    assert dequeue(q) is None
    assert len(q) == 0