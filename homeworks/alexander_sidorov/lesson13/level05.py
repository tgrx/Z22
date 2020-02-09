from typing import Any
from typing import Callable
from urllib.parse import urlparse

from .level04 import Response


class Server:
    class Redirect(Exception):
        pass

    class NotFound(Exception):
        pass

    def __init__(self, host):
        self.__host = host
        self.__handlers = {}

    def add_handler(self, path: str, handler: Callable):
        path_normal = self._normalize_path(path)
        self.__handlers[path_normal] = handler

    def serve(self, url):
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            parsed_url = urlparse(f"http://{url}")

        response = self._dispatch(parsed_url)

        return str(response)

    def _normalize_path(self, path_raw):
        path_normal = path_raw.replace(self.__host, "")

        if path_normal and path_normal[-1] == "/":
            path_normal = path_normal[:-1]

        return path_normal

    def _dispatch(self, url: Any):
        code = 200
        payload = None

        try:
            payload = self._handle(url)
        except self.Redirect:
            code = 302
        except self.NotFound:
            code = 404
        except Exception as err:
            code = 500
            payload = str(err)

        return Response(code=code, body=payload)

    def _handle(self, url):
        handler = self._get_handler(url)
        payload = handler(self, url)

        return payload

    def _get_handler(self, url):
        self._verify_handler_found_for(url)

        path = self._normalize_path(url.path)

        return self.__handlers[path]

    def _verify_handler_found_for(self, url):
        if url.hostname != self.__host:
            raise self.NotFound(f"unknown host: `{url.hostname}`")

        path = self._normalize_path(url.path)

        if path not in self.__handlers:
            raise self.NotFound(f"no handler for `{path}`")
