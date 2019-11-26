import platform
import typing


def fnc4():
    name = input("Enter your name")
    return f"Hello {name} !"


SWITCHER = {
    1: "Hello world",
    2: "My name is Yan. I'm student of BSUIR', 29.07.2000",
    3: platform.uname(),
    4: {fnc4},
}
RESULT = SWITCHER[int(input("Enter number"))]
if isinstance(RESULT, typing.Callable):
    print(RESULT())
else:
    print(RESULT)
