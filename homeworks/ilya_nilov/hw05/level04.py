from urllib.parse import urlparse
from urllib.parse import re


def host(hstnam):

    if not hstnam:
        return ""
    if "http" in hstnam:
        return urlparse(hstnam).netloc
    if "@" in hstnam:
        return re.findall(r"@\w+.\w+", hstnam)[0][1:]
    return hstnam.split("/")[0]
