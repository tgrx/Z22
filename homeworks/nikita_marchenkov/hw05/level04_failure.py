from urllib.parse import urlparse
import re


def host(url):
    if not url:
        return False
    if "@" in url:
        result = re.findall(r"@\w+.\w+", url)
        result = result[0][1:]
        return result
    if "http" in url:
        return urlparse(url).netloc

    return url.split("/")[0]
