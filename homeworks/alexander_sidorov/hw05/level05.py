from typing import Collection


def unique(collection: Collection) -> bool:
    return len(collection) == len(set(collection))
