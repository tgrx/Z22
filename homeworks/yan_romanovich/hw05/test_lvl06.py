from homeworks.yan_romanovich.hw05 import level06


def test():
    qaw = []

    assert level06.enqueue(qaw, 100) is None
    assert level06.enqueue(qaw, 200) is None
    assert len(qaw) == 2

    assert level06.dequeue(qaw) == 100
    assert len(qaw) == 1

    assert level06.enqueue(qaw, 300) is None
    assert len(qaw) == 2

    assert level06.dequeue(qaw) == 200
    assert level06.dequeue(qaw) == 300
    assert len(qaw) == 0

    assert level06.dequeue(qaw) is None
    assert len(qaw) == 0
