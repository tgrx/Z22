from homeworks.kirill_shevchuk.hw05.level02 import hello


def test_hello():
    assert hello("") == "Hi!"
    assert hello("Alex") == "Hello, Alex!"
    assert hello(None) == "Hi!"
