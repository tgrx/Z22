from typing import Dict


def verify_meta(meta):
    if not meta:
        raise ValueError("malformed response: no meta")


def get_headers(response: str) -> Dict[str, str]:
    result = {}

    if not response:
        return result

    meta, *_body = response.split("\n\n")
    verify_meta(meta)

    for line in meta.split("\n"):
        header, *values = line.split(": ")
        if not values or len(values) > 1:
            continue

        value = values[0].strip()

        result[header.strip()] = value

    return result
