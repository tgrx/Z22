from typing import Dict
from typing import TypeVar

QueueElementT = TypeVar("QueueElementT")


def enqueue(
    queue: Dict[int, QueueElementT], priority: int, element: QueueElementT
) -> None:
    queue.setdefault(priority, []).insert(0, element)


def dequeue(queue: Dict[int, QueueElementT]) -> QueueElementT:
    if not queue:
        return None

    priority = max(queue)
    line = queue.get(priority, [])
    element = line.pop() if line else None

    if not line:
        del queue[priority]

    return element
