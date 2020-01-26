from typing import Any
from typing import Dict
from typing import Text

import pytest

from project.settings import HOMEWORKS
from project.utils import import_by_path


def find_modules_for_level(level: Text) -> Dict[Text, Any]:
    modules = {}

    for pyfile in HOMEWORKS.glob(f"**/lesson09/{level}.py"):
        student = pyfile.parts[-3]
        module = import_by_path(pyfile)
        modules[student] = module

    return modules


@pytest.fixture
def modules_level01() -> Dict[Text, Any]:
    return find_modules_for_level("level01")


@pytest.fixture
def modules_level02() -> Dict[Text, Any]:
    return find_modules_for_level("level02")
