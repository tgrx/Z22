from homeworks.vladimir_lepeshko.hw05.level06 import enqueue, dequeue


def test():
    queue_original = queue = []

    assert enqueue(queue, 100) is None
    assert enqueue(queue, 200) is None
    assert len(queue) == 2

    assert dequeue(queue) == 100
    assert len(queue) == 1

    assert enqueue(queue, 300) is None
    assert len(queue) == 2

    assert dequeue(queue) == 200
    assert dequeue(queue) == 300
    assert len(queue) == 0

    assert dequeue(queue) is None
    assert len(queue) == 0

    assert queue_original is queue
