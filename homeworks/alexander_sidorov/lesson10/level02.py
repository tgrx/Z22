from typing import Collection


def plus_minus(numbers: Collection[int]) -> str:
    positives = negatives = zeroes = 0
    total = len(numbers)

    for number in numbers:
        positives += number > 0
        negatives += number < 0
        zeroes += number == 0

    positives /= total
    negatives /= total
    zeroes /= total

    return "\n".join(f"{_r:.6f}" for _r in (positives, negatives, zeroes))
