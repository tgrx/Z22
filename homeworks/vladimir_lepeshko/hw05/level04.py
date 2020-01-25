import re


def host(url):
    """ Host function """

    if url is None:
        return ""

    if "//" in url:
        return re.split(r"//(\w+.\w+)", url)[1]

    if "@" in url:
        return re.split(r"@(.\w+.\w+)", url)[1]

    else:
        return url.split("/")[0]
