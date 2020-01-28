# pylint: disable=C0103,R0124

from typing import Callable

import pytest

from lessons.lesson05.tests.test_level03 import BAD_PHONES
from . import test_level01 as regression01
from . import test_level02 as regression02
from . import test_level03 as regression03
from . import test_level04 as regression04


def verify_class_structure(klass):
    assert isinstance(klass, type)

    mro = klass.mro()
    assert len(mro) == 6
    assert mro[0] is klass
    regression04.verify_class_structure(mro[1])
    regression03.verify_class_structure(mro[2])
    regression02.verify_class_structure(mro[3])
    regression01.verify_class_structure(mro[4])
    assert mro[5] == object

    assert len(klass.__dict__) == 4
    assert "__init__" in klass.__dict__
    assert "__eq__" not in klass.__dict__
    assert "validate" in klass.__dict__
    assert hasattr(klass, "validate")
    assert isinstance(getattr(klass, "validate"), Callable)


def verify_class_init(klass):
    with pytest.raises(TypeError):
        klass()
    with pytest.raises(TypeError):
        klass(1)
    with pytest.raises(TypeError):
        klass(1, 2)
    with pytest.raises(TypeError):
        klass(name=1)
    with pytest.raises(TypeError):
        klass(email=1)
    with pytest.raises(TypeError):
        klass(1, 2, name=1, email=2)
    with pytest.raises(TypeError):
        klass(1, 2, 3, 4)
    with pytest.raises(TypeError):
        klass(1, 2, 3, phone=4)
    with pytest.raises(TypeError):
        klass(name=1, email=2, phone=3, password=4)

    user = klass(1, 2, 3)
    assert user.__dict__ == {"name": 2, "email": 3, "phone": 1}

    user = klass(name=False, email=None, phone=True)
    assert user.__dict__ == {"name": False, "email": None, "phone": True}


def verify_class_validate_method(klass):
    regression04.verify_validate_method(klass, phone="+375292020327")

    for bad_phone in BAD_PHONES:
        with pytest.raises(ValueError):
            user = klass(name="ok", email="ok@ok.ok", phone=bad_phone)
            user.validate()


def verify_class(klass):
    verify_class_structure(klass)
    verify_class_init(klass)
    regression03.verify_class_comparison(klass, phone=1)
    verify_class_validate_method(klass)


def verify_module(module):
    class_name = "User"

    assert hasattr(module, class_name)

    User = getattr(module, class_name)
    verify_class(User)


def test(modules_level05):
    for module in modules_level05.values():
        verify_module(module)
