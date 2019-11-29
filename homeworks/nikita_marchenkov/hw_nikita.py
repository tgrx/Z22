VARIANT = int(
    input(
        """Write the number of variant you want see on the screen:
1 - Show phrase \"Hello, World\"
2 - Information about yourself
3 - Information about your system
4 - Greeting
"""
    )
)
if VARIANT == 1:
    print("Hello, World")
elif VARIANT == 2:
    import getpass

    print("Information about yourself: " + getpass.getuser())
elif VARIANT == 3:
    import sysconfig

    print("Information about your system: " + sysconfig.get_platform())
elif VARIANT == 4:
    NAME = input("Write your name, please:")
    print(f"Welcome, {NAME}!")
else:
    print("What a pity, there is no such variant!")
