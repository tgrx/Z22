"""Уровень 6"""


def enqueue(queue, elm):
    """Функция принимает элемент"""
    queue.append(elm)


def dequeue(queue):
    """Функция достает элемент"""
    if not queue:
        return None
    return queue.pop(0)
