from urllib.parse import urlparse
from homeworks.kirill_shevchuk.lesson13 import level04


class Server:
    class Redirect(Exception):
        pass

    def __init__(self, host):
        self.host = host
        self.heandlers = {}

    def add_handler(self, road, heandler):
        url = self.host + road
        self.heandlers[url] = heandler

    def serve(self, url_1):
        url = urlparse(url_1)
        host_path = url.netloc + url.path
        if host_path[-1] == "/":
            host_path = host_path[:-1]
        body = None
        try:
            body = self.heandlers[host_path](self, url)
        except KeyError:
            code = 404
        except self.Redirect:
            code = 302
        except Exception as err:
            body = str(err)
            code = 500
        else:
            code = 200
        return str(level04.Response(body=body, code=code))
