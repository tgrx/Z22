def host(hstnam):
    import tldextract

    if not hstnam:
        return " "
    listurl = tldextract.extract(hstnam)
    if listurl.domain == "" and listurl.suffix == "":
        return ""
    else:
        return f"{listurl.domain}.{listurl.suffix}"
