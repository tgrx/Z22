from homeworks.yan_romanovich.lesson11 import level01


def test():
    assert isinstance(level01.User, type)
    assert level01.User.mro() == [level01.User, object]
    assert len(level01.User.__dict__) == 4
    assert hasattr(level01.User, "__init__")
    assert "__init__" not in level01.User.__dict__
    assert level01.User().__dict__ == {}
