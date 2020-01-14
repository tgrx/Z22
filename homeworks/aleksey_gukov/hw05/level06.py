def enqueue(lst, element):
    lst.append(element)


def dequeue(lst):
    if not lst:
        return None
    return lst.pop(0)
