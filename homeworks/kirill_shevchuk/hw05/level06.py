def enqueue(turn, last):
    turn.append(last)


def dequeue(turn):
    return None if not turn else turn.pop(0)
