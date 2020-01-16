from urllib.parse import urlparse


def host(url):
    if not url:
        return ""
    data = urlparse(url)
    if data.netloc:
        return data.netloc
    value = data.path.split("/")[0]
    if "@" not in value or ":" not in value:
        return value
    from_ = value.find("@") + 1
    for_ = value.find(":")
    return value[from_:for_]
