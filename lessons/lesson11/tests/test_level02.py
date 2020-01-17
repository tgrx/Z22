# pylint: disable=C0103

import pytest


def verify(module):
    class_name = "User"

    assert hasattr(module, class_name)

    User = getattr(module, class_name)
    assert isinstance(User, type)
    assert len(User.mro()) == 3
    assert User.mro()[0] == User
    assert User.mro()[-1] == object
    assert len(User.__dict__) == 3
    assert "__init__" in User.__dict__

    with pytest.raises(TypeError):
        User()
    with pytest.raises(TypeError):
        User(1)
    with pytest.raises(TypeError):
        User(name=1)
    with pytest.raises(TypeError):
        User(email=1)

    user = User(name=False, email=None)
    assert user.__dict__ == {"name": False, "email": None}


def test(modules_level02):
    for module in modules_level02.values():
        verify(module)
