from typing import Any, List


def enqueue(queue: List, elm: Any) -> None:
    queue.insert(0, elm)


def dequeue(queue: List) -> Any:
    return queue.pop() if queue else None
