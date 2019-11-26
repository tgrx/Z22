VARIANT = ""
while VARIANT not in ("1", "2", "3", "4"):
    VARIANT = input(
        'What do you want(1,2,3 or 4)? (1-"Hello, World",2-user info,3-system info,4-greeting): '
    )
if VARIANT == "1":
    print("Hello, World")
elif VARIANT == "2":
    import os

    print("Current user: " + os.getlogin())
elif VARIANT == "3":
    import platform

    print("Your system: " + platform.system())
elif VARIANT == "4":
    NAME = input("What is your name?:")
    print("Hello, " + NAME + "!")
else:
    print("error")
