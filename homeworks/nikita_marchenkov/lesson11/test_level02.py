from homeworks.nikita_marchenkov.lesson11 import level02


def test():
    obj = level02.User("Nikita", "erastfandorin228@mail.ru")
    assert isinstance(obj, level02.User)
    assert obj.name
    assert obj.email
