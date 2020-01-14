from homeworks.nikita_marchenkov.hw05 import level06


def test():
    q_q = []

    assert level06.enqueue(q_q, 100) is None
    assert level06.enqueue(q_q, 200) is None
    assert len(q_q) == 2

    assert level06.dequeue(q_q) == 100
    assert len(q_q) == 1

    assert level06.enqueue(q_q, 300) is None
    assert len(q_q) == 2

    assert level06.dequeue(q_q) == 200
    assert level06.dequeue(q_q) == 300
    assert len(q_q) == 0

    assert level06.dequeue(q_q) is None
    assert len(q_q) == 0
