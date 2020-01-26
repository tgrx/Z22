from typing import Any
from typing import Dict
from typing import Text

import pytest

from project.settings import HOMEWORKS
from project.utils import import_by_path

_BENZAK_HTTP_RESPONSE = """HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 4053
Content-Type: text/html; charset=utf-8
Date: Sun, 26 Jan 2020 14:07:02 GMT
Server: gunicorn/19.9.0
Vary: Cookie
Via: 1.1 vegur
X-Frame-Options: SAMEORIGIN

<!DOCTYPE html>
<html lang="ru">
<head>
</head>
<body>
<pre>
    HTTP/1.1 200 OK
Connection: keep-alive
    Content-Length: 4053
Content-Type: text/html; charset=utf-8
    Date: Sun, 26 Jan 2020 14:07:02 GMT
Server: gunicorn/19.9.0
    Vary: Cookie
Via: 1.1 vegur
    X-Frame-Options: SAMEORIGIN
</pre>
</body>
</html>
"""


def find_modules_for_level(level: Text) -> Dict[Text, Any]:
    modules = {}

    for pyfile in HOMEWORKS.glob(f"**/lesson13/{level}.py"):
        student = pyfile.parts[-3]
        module = import_by_path(pyfile)
        modules[student] = module

    return modules


@pytest.fixture
def benzak_http_response() -> str:
    return _BENZAK_HTTP_RESPONSE


@pytest.fixture
def modules_level01() -> Dict[Text, Any]:
    return find_modules_for_level("level01")


@pytest.fixture
def modules_level02() -> Dict[Text, Any]:
    return find_modules_for_level("level02")


@pytest.fixture
def modules_level03() -> Dict[Text, Any]:
    return find_modules_for_level("level03")


@pytest.fixture
def modules_level04() -> Dict[Text, Any]:
    return find_modules_for_level("level04")


@pytest.fixture
def modules_level05() -> Dict[Text, Any]:
    return find_modules_for_level("level05")
