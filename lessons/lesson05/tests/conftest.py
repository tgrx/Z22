from typing import Any, Dict, Text

import pytest

from project.settings import HOMEWORKS
from project.utils import import_by_path


def find_modules_for_level(level: Text) -> Dict[Text, Any]:
    modules = {}

    for pyfile in HOMEWORKS.glob(f"**/hw05/{level}.py"):
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


@pytest.fixture
def modules_level03() -> Dict[Text, Any]:
    return find_modules_for_level("level03")


@pytest.fixture
def modules_level04() -> Dict[Text, Any]:
    return find_modules_for_level("level04")


@pytest.fixture
def modules_level05() -> Dict[Text, Any]:
    return find_modules_for_level("level05")


@pytest.fixture
def modules_level06() -> Dict[Text, Any]:
    return find_modules_for_level("level06")


@pytest.fixture
def modules_level07() -> Dict[Text, Any]:
    return find_modules_for_level("level07")
