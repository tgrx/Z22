import re


def host(url):
    """QWERTYUIO"""
    if url is not None:
        result = re.search(r"(\w+\.\w+).+$", url)
        if result is None:
            return ""
        return result.group(1)
    return False
