from homeworks.ilya_nilov.hw05.level02 import hello


def test():
    assert hello("") == "Hi!"
    assert hello("Alex") == "Hello, Alex!"
    assert hello(None) == "Hi!"
