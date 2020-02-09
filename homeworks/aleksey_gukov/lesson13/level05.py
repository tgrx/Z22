from urllib.parse import urlparse
from homeworks.aleksey_gukov.lesson13 import level04


class Server:
    class Redirect(Exception):
        pass

    def __init__(self, host):
        self.host = host
        self.dict_path = {}

    def add_handler(self, path, handler):
        url_dict = self.host + path
        self.dict_path[url_dict] = handler

    def serve(self, url):
        text = ""
        url_rasp = urlparse(url)
        url_search = url_rasp.netloc + url_rasp.path
        if url_search and url_search[-1] == "/":
            url_search = url_search[:-1]
        if url_search in self.dict_path:
            create_text = self.dict_path[url_search]
            try:
                text = create_text(self, url_rasp)
            except self.Redirect:
                code = 302
            except Exception as error:
                code = 500
                text = str(error)
            else:
                code = 200
        else:
            code = 404
        answer = str(level04.Response(body=text, code=code))
        return answer
