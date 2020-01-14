def enqueue(lst, tms):
    lst.append(tms)


def dequeue(lst):
    if not lst:
        return None
    return lst.pop(0)
