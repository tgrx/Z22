import platform


def hello():
    print("Hello World")


def informathion():
    print(
        """   My name is Kirill
    I am from Belarus
    I am student of Belarusian State University informatics and radioelectronics"""
    )


def name_1():
    print("What is your name?")
    name = input()
    print("Hello", name)


def operation_system():
    print("Your OS it is ", platform.system())


def test(var):
    if var == 1:
        hello()
    elif var == 2:
        informathion()
    elif var == 3:
        operation_system()
    elif var == 4:
        name_1()


while True:
    print(
        """    1. Output "Hello, World"
    2. Information about creator
    3. Your operation system
    4. Hello user
    5. Exit
    Enter the number action you want to do"""
    )
    VARIANT = int(input())
    if VARIANT == 5:
        break
    while VARIANT > 5:
        print("Not such action. Please write again")
        VARIANT = int(input())
    test(VARIANT)
