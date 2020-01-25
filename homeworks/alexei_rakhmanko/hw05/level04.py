"""Уровень 4"""


def host(url):
    """Функция парсинга URl"""
    result = [url]
    if url is None:
        return ""
    if "@" in url:
        result[0] = result[0].split("@")[1]
    if "http" in url:
        result[0] = result[0].split("/")[2]
    if ":" in url:
        result[0] = result[0].split(":")[0]
    if "." in result[0]:
        return result[0].split("/")[0]
    return ""
