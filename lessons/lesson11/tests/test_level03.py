# pylint: disable=C0103,R0124

import pytest


def verify(module):
    class_name = "User"

    assert hasattr(module, class_name)

    User = getattr(module, class_name)
    assert isinstance(User, type)
    assert len(User.mro()) == 4
    assert User.mro()[0] == User
    assert User.mro()[-1] == object
    assert len(User.__dict__) == 4
    assert "__init__" not in User.__dict__
    assert "__eq__" in User.__dict__

    with pytest.raises(TypeError):
        User()
    with pytest.raises(TypeError):
        User(1)
    with pytest.raises(TypeError):
        User(name=1)
    with pytest.raises(TypeError):
        User(email=1)

    user1 = User(name=1, email=2)
    assert user1.__dict__ == {"name": 1, "email": 2}

    user2 = User(name=2, email=2)
    assert user2.__dict__ == {"name": 2, "email": 2}

    user3 = User(name=2, email=3)
    assert user3.__dict__ == {"name": 2, "email": 3}

    assert user1 == user1
    assert user2 == user2
    assert user3 == user3

    assert user1 == user2
    assert user2 == user1

    assert not user1 == user3
    assert not user3 == user1

    assert not user2 == user3
    assert not user3 == user2


def test(modules_level03):
    for module in modules_level03.values():
        verify(module)
