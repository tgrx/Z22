from homeworks.aleksey_gukov.lesson11 import level02


def test():
    obj = level02.User("Aleksey", "gukov@open.by")
    assert obj.name
    assert obj.email
    assert isinstance(obj, level02.User)
