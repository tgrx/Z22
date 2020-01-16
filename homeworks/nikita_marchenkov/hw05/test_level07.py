from homeworks.nikita_marchenkov.hw05 import level07


def test():
    unknown = {}
    assert level07.dequeue(unknown) is None
    assert level07.enqueue(unknown, 1, "a") is None
    assert level07.enqueue(unknown, 1, "b") is None
    assert level07.enqueue(unknown, 2, "aa") is None
    assert level07.dequeue(unknown) == "aa"
    assert level07.enqueue(unknown, 1, "c") is None
    assert level07.enqueue(unknown, 3, "aaa") is None
    assert level07.enqueue(unknown, 3, "bbb") is None
    assert level07.enqueue(unknown, 2, "bb") is None
    assert level07.dequeue(unknown) == "aaa"
    assert level07.dequeue(unknown) == "bbb"
    assert level07.dequeue(unknown) == "bb"
    assert level07.dequeue(unknown) == "a"
    assert level07.dequeue(unknown) == "b"
    assert level07.dequeue(unknown) == "c"
    assert level07.dequeue(unknown) is None
    assert unknown == {}
