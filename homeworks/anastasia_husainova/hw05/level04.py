import re


def cut_scheme(url):
    separator = "//"

    if separator not in url:
        return url

    parts = re.split(separator, url)

    return parts[1]


def cut_userinfo(url) -> str:
    separator = "@"

    if separator not in url:
        return url

    parts = re.split(separator, url)
    return parts[1]


def cut_port(url):
    separator = ":"

    if separator not in url:
        return url

    parts = re.split(separator, url)

    return parts[0]


def cut_path(url):
    separator = "/"

    if separator not in url:
        return url

    parts = re.split(separator, url)

    return parts[0]


def host(url):
    if not url:
        return ""

    authority_path = cut_scheme(url)
    hostname_port_path = cut_userinfo(authority_path)
    hostname_port = cut_path(hostname_port_path)
    hostname = cut_port(hostname_port)
    return hostname


if __name__ == "__main__":
    H = host("ftp://gist.github.com")
    print(H)
