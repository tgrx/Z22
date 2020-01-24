from homeworks.yan_romanovich.lesson11 import level02


def test():
    assert isinstance(level02.User, type)
    assert len(level02.User.mro()) == 3
    assert level02.User.mro()[0] == level02.User
    assert level02.User.mro()[-1] == object
    assert len(level02.User.__dict__) == 3
    assert "__init__" in level02.User.__dict__
