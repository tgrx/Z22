from homeworks.nikita_marchenkov.lesson11 import level03


def test():
    obj_a = level03.User("Nikita", "erastfandorin228@mail.ru")
    obj_b = level03.User("Petr", "erastfandorin228@mail.ru")
    assert obj_a == obj_b
