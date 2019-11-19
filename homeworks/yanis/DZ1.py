import platform

def fnc4():
    Name=input("Enter your name - ")
    return Name

def fnc(argument):
            switcher = {
                1:"Hello world",
                2:"My name is Yan. I'm student of BSUIR', 29.07.2000",
                3: platform.uname(),
                4: fnc4(),
            }
            return switcher.get(argument, "Incorrect value")
Nomer_varianta =int(input("Enter number 1-4: "))
print(fnc(Nomer_varianta))







