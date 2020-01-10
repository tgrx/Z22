from typing import Text


def hello(name: Text) -> Text:
    if not name:
        return "Hi!"
    return f"Hello, {name}!"
