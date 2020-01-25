from urllib.parse import urlparse


def host(url):
    result = urlparse(url)
    if result.netloc:
        return result.netloc
    if not url:
        return ""
    res = result.path.split("/")[0]
    if ":" not in res or "@" not in res:
        return res
    from_ = res.find("@") + 1
    for_ = res.find(":")
    return res[from_:for_]
