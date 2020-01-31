# pylint: disable=C0103,R0124

from typing import Callable

import pytest

from . import test_level01 as regression01
from . import test_level02 as regression02
from . import test_level03 as regression03


def must_be_invalid(user):
    with pytest.raises(ValueError):
        user.validate()


def must_be_valid(user):
    try:
        user.validate()
    except Exception:
        raise AssertionError


def verify_class_structure(klass):
    assert isinstance(klass, type)

    mro = klass.mro()
    assert len(mro) == 5
    assert mro[0] == klass
    regression03.verify_class_structure(mro[1])
    regression02.verify_class_structure(mro[2])
    regression01.verify_class_structure(mro[3])
    assert mro[4] is object

    assert len(klass.__dict__) == 3
    assert "__eq__" not in klass.__dict__
    assert "__init__" not in klass.__dict__
    assert "validate" in klass.__dict__
    assert isinstance(getattr(klass, "validate"), Callable)


def verify_validate_invalid_name(klass, **kw):
    must_be_invalid(klass(name="", email="good@email.com", **kw))
    must_be_invalid(klass(name="1a", email="good@email.com", **kw))
    must_be_invalid(klass(name="A", email="good@email.com", **kw))
    must_be_invalid(klass(name="a1A-", email="good@email.com", **kw))
    must_be_invalid(klass(name="лул", email="good@email.com", **kw))


def verify_validate_invalid_email_name(klass, **kw):
    must_be_invalid(klass(name="goodname1", email="1a@host.com", **kw))
    must_be_invalid(klass(name="goodname1", email="@host.com", **kw))
    must_be_invalid(klass(name="goodname1", email="A@host.com", **kw))
    must_be_invalid(klass(name="goodname1", email="a1A-@host.com", **kw))
    must_be_invalid(klass(name="goodname1", email="лул@host.com", **kw))


def verify_validate_invalid_email_host(klass, **kw):
    must_be_invalid(klass(name="goodname1", email="goodname1@.", **kw))
    must_be_invalid(klass(name="goodname1", email="goodname1@.a", **kw))
    must_be_invalid(klass(name="goodname1", email="goodname1@1", **kw))
    must_be_invalid(klass(name="goodname1", email="goodname1@1a", **kw))
    must_be_invalid(klass(name="goodname1", email="goodname1@a.", **kw))
    must_be_invalid(klass(name="goodname1", email="goodname1@a@a", **kw))


def verify_validate_invalid_email(klass, **kw):
    must_be_invalid(klass(name="goodname1", email="", **kw))
    must_be_invalid(klass(name="goodname1", email="@", **kw))
    must_be_invalid(klass(name="goodname1", email="@host", **kw))
    must_be_invalid(klass(name="goodname1", email="name@", **kw))

    verify_validate_invalid_email_name(klass, **kw)
    verify_validate_invalid_email_host(klass, **kw)


def verify_validate_valid_name_email(klass, **kw):
    must_be_valid(klass(name="a", email="a@a", **kw))
    must_be_valid(klass(name="name", email="name@HOST", **kw))
    must_be_valid(klass(name="name", email="name@host", **kw))
    must_be_valid(klass(name="name1", email="name1@host1", **kw))
    must_be_valid(klass(name="name1", email="name1@host1.b.com", **kw))
    must_be_valid(klass(name="name1", email="name1@host1.com", **kw))
    must_be_valid(klass(name="zz9", email="zz9@zz9", **kw))


def verify_validate_method(klass, **kw):
    verify_validate_invalid_name(klass, **kw)
    verify_validate_invalid_email(klass, **kw)
    verify_validate_valid_name_email(klass, **kw)


def verify_class(klass):
    verify_class_structure(klass)
    regression02.verify_class_init(klass)
    regression03.verify_class_comparison(klass)
    verify_validate_method(klass)


def verify_module(module):
    class_name = "User"
    assert hasattr(module, class_name)

    User = getattr(module, class_name)
    verify_class(User)


def test(modules_level04):
    for module in modules_level04.values():
        verify_module(module)
