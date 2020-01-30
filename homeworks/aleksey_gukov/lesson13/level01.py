def get_headers(http_resp):
    spisok = http_resp.split("\n")
    del spisok[0]
    del spisok[spisok.index("") :]
    slovar = {}
    for chast in spisok:
        head = chast.split(": ")
        slovar[head[0]] = head[1]
    return slovar
