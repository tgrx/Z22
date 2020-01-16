from homeworks.nikita_marchenkov.hw05 import level04_failure


def test():
    assert level04_failure.host("test.com/a/b/c") == "test.com"
    assert not level04_failure.host("/a/b")
    assert level04_failure.host("/a/b") == ""

    assert level04_failure.host("https://github.com/tgrx/Z22/") == "github.com"
    assert level04_failure.host("git@github.com:tgrx/Z22.git") == "github.com"
