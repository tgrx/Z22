import platform

def fnc4():
    Name=input("fvgbhnjmk")
    return Name

def fnc(argument):
            switcher = {
                1:"Hello world",
                2:"My name is Yan. I'm student of BSUIR', 29.07.2000",
                3: platform.uname(),
                4: fnc4(),
            }
            return switcher.get(argument, "Неверное значение")
Nomer_varianta =int(input("Введите номер варианта 1-4:"))
result = fnc(Nomer_varianta)
print(result)







