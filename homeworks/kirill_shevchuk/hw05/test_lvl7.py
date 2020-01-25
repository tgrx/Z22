from homeworks.kirill_shevchuk.hw05.level07 import dequeue, enqueue


def test():
    queue_original = queue = {}
    assert dequeue(queue) is None
    assert enqueue(queue, 1, "a") is None
    assert enqueue(queue, 1, "b") is None
    assert enqueue(queue, 2, "aa") is None
    assert dequeue(queue) == "aa"
    assert enqueue(queue, 1, "c") is None
    assert enqueue(queue, 3, "aaa") is None
    assert enqueue(queue, 3, "bbb") is None
    assert enqueue(queue, 2, "bb") is None
    assert dequeue(queue) == "aaa"
    assert dequeue(queue) == "bbb"
    assert dequeue(queue) == "bb"
    assert dequeue(queue) == "a"
    assert dequeue(queue) == "b"
    assert dequeue(queue) == "c"
    assert dequeue(queue) is None
    assert queue == {}
    assert queue is queue_original
