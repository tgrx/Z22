from homeworks.nikita_marchenkov.lesson13.level03 import make_headers


class Response:
    def __init__(self, code=200, headers="", body=""):
        self.code = code
        self.headers = headers
        self.body = body

    def __str__(self):
        dictionary = {
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

        true_response = f"HTTP/1.1 {self.code} {dictionary[self.code]}\n"
        if self.headers:
            true_response = true_response + f"{make_headers(self.headers)}\n"
        if self.body:
            true_response = true_response + f"\n{self.body}"
        return true_response
