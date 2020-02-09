from homeworks.ilya_nilov.lesson13.level03 import make_headers


class Response:
    def __init__(self, code=200, headers: str = "", body: str = ""):
        self.code = code
        self.headers = headers
        self.body = body

    def __str__(self):
        return f"""HTTP/1.1 {self.code} {http_codes(self.code)}
{is_validate_header(self.headers)}{is_validate_body(self.body)}"""


# можно ли как-то "отловить", что именно передается в функцию из вне?
# (self.headers или self.body)
def is_validate_header(http_particle):
    if http_particle:
        return make_headers(http_particle) + "\n"
    return ""  # и можно ли ничего не возвращать, или что будет корректнее?


def is_validate_body(http_particle):
    if http_particle:
        return "\n" + http_particle
    return ""


def http_codes(code):
    codes = {
        100: "Continue",
        101: "Switching Protocol",
        102: "Processing",
        103: "Early Hints",
        200: "OK",
        201: "Created",
        202: "Accepted",
        203: "Non-Authoritative Information",
        204: "No Content",
        205: "Reset Content",
        206: "Partial Content",
        300: "Multiple Choice",
        301: "Moved Permanently",
        302: "Found",
        400: "Bad Request",
        401: "Unauthorized",
        402: "Payment Required",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        500: "Internal Server Error",
    }
    return codes[code]
