from homeworks.vladimir_lepeshko.hw05.level04 import host


def test_host():
    assert host("/a/b") == ""
    assert host("git@github.com:tgrx/Z22.git") == "github.com"
    assert host("https://github.com/tgrx/Z22/") == "github.com"
    assert host("test.com/a/b/c") == "test.com"
    assert not host("")
    assert not host("/a/b")
    assert not host(None)
