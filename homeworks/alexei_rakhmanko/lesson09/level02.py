"""Уровень 2"""


def rotate_left(_sp, rev):
    """Функия вращения"""
    result = _sp[:]
    for _ in range(rev):
        result.append(result[0])
        result.pop(0)

    return result
