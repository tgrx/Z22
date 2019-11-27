from pathlib import Path

Z22 = Path(__file__).parent.parent.resolve()

HOMEWORKS: Path = Z22 / "homeworks"
LESSONS: Path = Z22 / "lessons"

assert HOMEWORKS.is_dir(), f"HOMEWORKS: {HOMEWORKS.as_posix()} is not a dir"
assert LESSONS.is_dir(), f"HOMEWORKS: {HOMEWORKS.as_posix()} is not a dir"
