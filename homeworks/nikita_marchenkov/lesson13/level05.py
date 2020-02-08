from urllib.parse import urlparse
from homeworks.nikita_marchenkov.lesson13.level04 import Response


class Server:
    class Redirect(Exception):
        pass

    def __init__(self, host):
        self.host = host
        self.dictionary = {}

    def add_handler(self, path, handler):
        self.dictionary[path] = handler

    def serve(self, url):
        result_handler = ""

        parsed_url = urlparse(url)
        host_url = parsed_url.netloc
        path_url = parsed_url.path
        if url[-1] == "/":
            path_url = path_url[:-1]
        if "://" not in url:
            result_split = path_url.split("/")
            path_url = "/" + result_split[-1]
            host_url = result_split[-2]

        if host_url == self.host and path_url in self.dictionary:
            try:
                code = 200
                call_handler = self.dictionary[path_url]
                result_handler = call_handler(self, parsed_url)
            except self.Redirect:
                code = 302
            except Exception as this_error:
                code = 500
                result_handler = str(this_error)
        else:
            code = 404
            result_handler = None

        return str(Response(body=result_handler, code=code))
