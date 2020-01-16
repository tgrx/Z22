from homeworks.nikita_marchenkov.hw05 import level02


def test():
    assert level02.hello("") == "Hi!"
    assert level02.hello("Alex") == "Hello, Alex!"
    assert level02.hello(None) == "Hi!"
