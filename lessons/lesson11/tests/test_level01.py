# pylint: disable=C0103

import pytest


def verify(module):
    class_name = "User"

    assert hasattr(module, class_name)

    User = getattr(module, class_name)
    assert isinstance(User, type)
    assert User.mro() == [User, object]
    assert len(User.__dict__) == 4
    assert hasattr(User, "__init__")
    assert "__init__" not in User.__dict__

    with pytest.raises(TypeError):
        User(1)
    with pytest.raises(TypeError):
        User(1, 2)
    with pytest.raises(TypeError):
        User(name=1)
    with pytest.raises(TypeError):
        User(email=1)

    user = User()
    assert user.__dict__ == {}


def test(modules_level01):
    for module in modules_level01.values():
        verify(module)
