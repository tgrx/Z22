# pylint: disable=C0103,R0124

from typing import Callable

import pytest


def verify(module):
    class_name = "User"

    assert hasattr(module, class_name)

    User = getattr(module, class_name)
    assert isinstance(User, type)
    assert len(User.mro()) == 6
    assert User.mro()[0] == User
    assert User.mro()[-1] == object
    assert len(User.__dict__) == 3
    assert hasattr(User, "validate")
    assert "__init__" in User.__dict__
    assert "__eq__" not in User.__dict__
    assert "validate" in User.__dict__
    assert isinstance(getattr(User, "validate"), Callable)

    with pytest.raises(TypeError):
        User()
    with pytest.raises(TypeError):
        User(1)
    with pytest.raises(TypeError):
        User(name=1)
    with pytest.raises(TypeError):
        User(email=1)

    user1 = User(name="a", email="a@a.a", phone="+375292020327a")
    assert user1.__dict__ == dict(name="a", email="a@a.a", phone="+375292020327a")
    with pytest.raises(ValueError) as exc:
        user1.validate()
        assert str(exc)

    user2 = User(name="a", email="a@a.a", phone="+375292020327")
    assert user2.__dict__ == dict(name="a", email="a@a.a", phone="+375292020327")
    try:
        user2.validate()
    except Exception as exc:
        raise AssertionError from exc

    user3 = User(name=2, email=3, phone=3)
    assert user3.__dict__ == {"name": 2, "email": 3, "phone": 3}

    assert user1 == user1
    assert user2 == user2
    assert user3 == user3

    assert user1 == user2
    assert user2 == user1

    assert not user1 == user3
    assert not user3 == user1

    assert not user2 == user3
    assert not user3 == user2


def test(modules_level05):
    for module in modules_level05.values():
        verify(module)
