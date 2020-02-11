from homeworks.ilya_nilov.lesson13.level03 import make_headers


class Response:
    def __init__(self, code=200, headers: str = "", body: str = ""):
        self.code = code
        self.headers = headers
        self.body = body

    def __str__(self):
        return f"""HTTP/1.1 {self.code} {http_codes(self.code)}
{is_validate_header(self.headers)}{is_validate_body(self.body)}"""


def is_validate_header(http_particle):
    if http_particle:
        return make_headers(http_particle) + "\n"
    return ""


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
        303: "See Other",
        304: "Not Modified",
        305: "Use Proxy",
        306: "Switch Proxy",
        307: "Temporary Redirect",
        308: "Permanent Redirect",
        400: "Bad Request",
        401: "Unauthorized",
        402: "Payment Required",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        406: "Not Acceptable",
        407: "Proxy Authentication Required",
        408: "Request Timeout",
        409: "Conflict",
        410: "Gone",
        411: "Length Required",
        412: "Precondition Failed",
        413: "Request Entity Too Large",
        414: "Request-URI Too Long",
        415: "Unsupported Media Type",
        416: "Requested Range Not Satisfiable",
        417: "Expectation Failed",
        500: "Internal Server Error",
        501: "Not Implemented",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Timeout",
        505: "HTTP Version Not Supported",
    }
    return codes[code]
