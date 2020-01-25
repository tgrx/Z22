from typing import Sequence
from typing import TypeVar

ElmT = TypeVar("ElmT")
RowT = Sequence[ElmT]
MatrixT = Sequence[RowT]


def diag_diff(matrix: MatrixT) -> ElmT:
    rank = len(matrix)

    diff = 0

    for i in range(rank):
        j = rank - i - 1
        diff += matrix[i][i] - matrix[i][j]

    return abs(diff)
