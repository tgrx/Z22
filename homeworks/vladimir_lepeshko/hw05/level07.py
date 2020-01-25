from homeworks.vladimir_lepeshko.hw05 import level06

""" Queue by enqueue, dequeue functions"""


def enqueue(dict, priority, element):
    """ Queue by dict"""

    lane = dict.setdefault(priority, [])
    level06.enqueue(lane, element)


def dequeue(dict):
    """ Return first element or None"""

    if not dict:
        return None
    if not dict.get(max(dict.keys())):
        del dict[max(dict.keys())]
    return None if not dict else level06.dequeue(dict.get(max(dict.keys())))
