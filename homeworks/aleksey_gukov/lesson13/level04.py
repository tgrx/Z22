from homeworks.aleksey_gukov.lesson13 import level03


class Response:
    def __init__(self, code=200, headers=None, body=None):
        self.code = code
        self.headers = headers
        self.body = body

    def __str__(self):
        code_dict = {
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
        code_resp = f"{self.code} {code_dict[self.code]}"
        if self.headers and self.body:
            answer = f"HTTP/1.1 {code_resp}\n{level03.make_headers(self.headers)}\n\n{self.body}"
        elif self.body and not self.headers:
            answer = f"HTTP/1.1 {code_resp}\n\n{self.body}"
        elif self.headers and not self.body:
            answer = f"HTTP/1.1 {code_resp}\n{level03.make_headers(self.headers)}\n"
        else:
            answer = f"HTTP/1.1 {code_resp}\n"
        return answer
