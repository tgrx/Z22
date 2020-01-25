from typing import Iterable


def big_summa(*args):
    return sum(
        (big_summa(*list(elm)) if isinstance(elm, Iterable) else elm) for elm in args
    )
