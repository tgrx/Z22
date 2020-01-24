from homeworks.yan_romanovich.lesson11 import level03


def test():
    assert isinstance(level03.User, type)
    assert len(level03.User.mro()) == 4
    assert level03.User.mro()[0] == level03.User
    assert level03.User.mro()[-1] == object
    assert len(level03.User.__dict__) == 4
    assert "__init__" not in level03.User.__dict__
    assert "__eq__" in level03.User.__dict__

    user1 = level03.User(name=1, email=2)
    assert user1.__dict__ == {"name": 1, "email": 2}

    user2 = level03.User(name=2, email=2)
    assert user2.__dict__ == {"name": 2, "email": 2}

    user3 = level03.User(name=2, email=3)
    assert user3.__dict__ == {"name": 2, "email": 3}

    assert user1 == user2

    assert user1 != user3

    assert user2 != user3
