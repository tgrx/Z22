from homeworks.aleksey_gukov.hw05 import level06


def test():
    name_q = []

    assert level06.enqueue(name_q, 100) is None
    assert level06.enqueue(name_q, 200) is None
    assert len(name_q) == 2

    assert level06.dequeue(name_q) == 100
    assert len(name_q) == 1

    assert level06.enqueue(name_q, 300) is None
    assert len(name_q) == 2

    assert level06.dequeue(name_q) == 200
    assert level06.dequeue(name_q) == 300
    assert len(name_q) == 0

    assert level06.dequeue(name_q) is None
    assert len(name_q) == 0
