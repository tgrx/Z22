from homeworks.aleksey_gukov.hw05 import level07


def test():
    name_x = {}
    assert level07.dequeue(name_x) is None
    assert level07.enqueue(name_x, 1, "a") is None
    assert level07.enqueue(name_x, 1, "b") is None
    assert level07.enqueue(name_x, 2, "aa") is None
    assert level07.dequeue(name_x) == "aa"
    assert level07.enqueue(name_x, 1, "c") is None
    assert level07.enqueue(name_x, 3, "aaa") is None
    assert level07.enqueue(name_x, 3, "bbb") is None
    assert level07.enqueue(name_x, 2, "bb") is None
    assert level07.dequeue(name_x) == "aaa"
    assert level07.dequeue(name_x) == "bbb"
    assert level07.dequeue(name_x) == "bb"
    assert level07.dequeue(name_x) == "a"
    assert level07.dequeue(name_x) == "b"
    assert level07.dequeue(name_x) == "c"
    assert level07.dequeue(name_x) is None
    assert name_x == {}
