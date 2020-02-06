from homeworks.kirill_shevchuk.lesson13 import level03


_OTVET_DICT = {
    200: "OK",
    201: "Created",
    204: "No Content",
    301: "Moved Permanently",
    302: "Found",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    500: "Internal Server Error",
}


class Response:
    def __init__(self, body="", headers=None, code=200):
        self.body = body
        self.headers = headers
        self.code = code

    def __str__(self):
        http_str = f"HTTP/1.1 {self.code} {_OTVET_DICT[self.code]}\n"
        if self.headers:
            http_str += level03.make_headers(self.headers) + "\n"
        if self.body:
            http_str += "\n" + self.body
        return http_str
