from homeworks.alexander_sidorov.lesson13.level03 import make_headers

NAME_FOR_HTTP_CODE = {
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
    def __init__(self, code=200, headers=None, body=None):
        self.code = code
        self.headers = headers if isinstance(headers, dict) else {}
        self.body = body

    def __str__(self):
        parts = (
            f"HTTP/1.1 {self.code} {NAME_FOR_HTTP_CODE[self.code]}",
            make_headers(self.headers),
            "",
            self.body,
        )

        resp = "\n".join(filter(lambda _p: _p is not None, parts))

        return resp
