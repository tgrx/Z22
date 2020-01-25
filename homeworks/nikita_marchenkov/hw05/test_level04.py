from homeworks.nikita_marchenkov.hw05 import level04


def test():
    assert level04.host("test.com/a/b/c") == "test.com"
    assert not level04.host("/a/b")
    assert level04.host("/a/b") == ""

    assert level04.host("https://github.com/tgrx/Z22/") == "github.com"
    assert level04.host("git@github.com:tgrx/Z22.git") == "github.com"
