import platform

INFOSYS = platform.uname()
LISTWITHDATA = ["Hello world!", "Нилов Илья, 19 лет, студент", INFOSYS, "welcome"]
INPTNUMBR = int
while INPTNUMBR != range(0, 4):
    try:
        INPTNUMBR = int(input("Выберете 1-4:" + "\n")) - 1
    except ValueError:
        print("Неверное значение")
        continue
    assert INPTNUMBR in range(0, 4)
    if INPTNUMBR == 3:
        USRNAM = input("Ваше имя:")
        LISTWITHDATA[3] = "Welcome " + USRNAM + "!"
    ANSWR = LISTWITHDATA[INPTNUMBR]
    print(ANSWR)
