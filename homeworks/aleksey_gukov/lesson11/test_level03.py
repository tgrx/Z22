from homeworks.aleksey_gukov.lesson11 import level03


def test():
    obj_1 = level03.User("aleksey", "gukov@open.by")
    obj_2 = level03.User("nikita", "gukov@open.by")
    assert obj_1 == obj_2
    obj_3 = level03.User("aleksey", "gukov@open.by")
    obj_4 = level03.User("nikita", "nikita@open.by")
    assert obj_3 != obj_4
