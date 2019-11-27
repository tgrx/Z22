from typing import Callable


def verify(module):
    func_enqueue = "enqueue"
    func_dequeue = "dequeue"

    assert hasattr(module, func_enqueue)
    assert hasattr(module, func_dequeue)

    enqueue = getattr(module, func_enqueue)
    assert isinstance(enqueue, Callable)

    dequeue = getattr(module, func_dequeue)
    assert isinstance(dequeue, Callable)

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


def test(modules_level06):
    for module in modules_level06.values():
        verify(module)
