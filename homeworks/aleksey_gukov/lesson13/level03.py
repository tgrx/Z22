from datetime import datetime


def make_headers(slovar):
    for key, value in slovar.items():
        if key == "Content-Length":
            slovar[key] = str(value)
        if key == "Date":
            slovar[key] = str(datetime.strftime(value, "%a, %e %b %Y %H:%M:%S GMT"))
    headers = sorted(slovar)
    otvet = "\n".join(f"{chast}: {slovar[chast]}" for chast in headers)
    return otvet
