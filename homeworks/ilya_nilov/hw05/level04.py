def host(hstnam):
    from tldextract import extract


    if not hstnam:
        return " "
    listurl = tldextract.extract(hstnam)
    return listurl.domain + '.' + listurl.suffix