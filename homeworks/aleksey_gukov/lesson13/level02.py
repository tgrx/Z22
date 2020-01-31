from datetime import datetime
from homeworks.aleksey_gukov.lesson13 import level01


def get_typed_headers(http_resp):
    slovar = level01.get_headers(http_resp)
    for key, value in slovar.items():
        if key == "Content-Length":
            slovar[key] = int(value)
        if key == "Date":
            slovar[key] = datetime.strptime(value, "%a, %d %b %Y %H:%M:%S %Z")
    return slovar
