from homeworks.ilya_nilov.hw05.level06 import enqueue
from homeworks.ilya_nilov.hw05.level06 import dequeue


def test():
    q_lits = []

    assert enqueue(q_lits, 100) is None
    assert enqueue(q_lits, 200) is None
    assert len(q_lits) == 2

    assert dequeue(q_lits) == 100
    assert len(q_lits) == 1

    assert enqueue(q_lits, 300) is None
    assert len(q_lits) == 2

    assert dequeue(q_lits) == 200
    assert dequeue(q_lits) == 300
    assert len(q_lits) == 0

    assert dequeue(q_lits) is None
    assert len(q_lits) == 0
