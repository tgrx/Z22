import re
from typing import Text

HOST = re.compile(r"(.*://|\w+@)?(?P<host>[\w0-9_.]+).*")


def host(url: Text) -> Text:
    if not url:
        return ""

    match = HOST.match(url)
    if not match:
        return ""

    return match.groupdict().get("host")
