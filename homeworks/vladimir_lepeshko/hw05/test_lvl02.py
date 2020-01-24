from homeworks.vladimir_lepeshko.hw05.level02 import hello


def test_hello():
    assert hello("") == "Hi!"
    assert hello("Alex") == "Hello, Alex!"
    assert hello(None) == "Hi!"
