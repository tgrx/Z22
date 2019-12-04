def enqueue(fifo, elm):
    fifo.append(elm)


def dequeue(fifo):
    if not fifo:
        return None
    return fifo.pop(0)
