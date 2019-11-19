import platform


def fnc4():
    name = input("Enter your name")
    return name


def fnc(argument):
    switcher = {
        1: "Hello world",
        2: "My name is Yan. I'm student of BSUIR', 29.07.2000",
        3: platform.uname(),
        4: fnc4,
    }
    return switcher.get(argument, "Incorrect value")


NOMER_VARIANTA = int(input("Enter number 1-4:"))
RESULT = fnc(NOMER_VARIANTA)
print(RESULT)
