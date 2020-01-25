"""FiFO by enqueue, dequeue"""


def enqueue(queue, anytype):
    """ Queue realisation"""
    queue.append(anytype)


def dequeue(queue):
    """ Return anytype from queue"""
    return None if not queue else queue.pop(0)
