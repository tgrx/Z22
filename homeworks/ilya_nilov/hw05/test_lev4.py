from homeworks.ilya_nilov.hw05.level04 import host


def test():
    assert host("test.com/a/b/c") == "test.com"
    assert not host("/a/b")
    assert host("/a/b") == ""

    assert host("https://github.com/tgrx/Z22/") == "github.com"
    assert host("git@github.com:tgrx/Z22.git") == "github.com"