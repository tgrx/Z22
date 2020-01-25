variant = ""
while variant not in ("1", "2", "3", "4"):
    variant = input(
        'Выберите(1,2,3 или 4)? (1-"Hello, World",2-информация,3-система,4-приветствие): '
    )
if variant == "1":
    print("Hello, World")
elif variant == "2":
    print("Меня зовут Женя, 23 года, хочу изучить язык программирования python")
elif variant == "3":
    import platform

    print("Your system: " + platform.system())
elif variant == "4":
    a = input("Ваше имя?:")
    print("Привет, " + a + "!")
else:
    print("error")
