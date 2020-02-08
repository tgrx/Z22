from datetime import datetime
from functools import partial
from typing import Any
from typing import Dict
from typing import Optional

from .level02 import convert


def to_http_datetime(value: datetime):
    formatted = value.strftime("%a, %d %b %Y %H:%M:%S GMT")
    parts = f"{formatted}".split(" ")
    parts[1] = parts[1].replace("0", " ")
    result = " ".join(parts)
    return result


CONVERTERS = {
    "Date": to_http_datetime,
}


def make_headers(headers: Dict[str, Any]) -> Optional[str]:
    conv = partial(convert, CONVERTERS, default=str)

    headers_lines = (
        f"{header}: {conv(header, value).strip()}"
        for header, value in sorted(headers.items())
        if value
    )

    result = "\n".join(headers_lines)

    return result or None
