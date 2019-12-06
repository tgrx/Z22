"""homework"""
import platform


def func():
    """Функция ввода имени"""
    _name = input("\n\tВведите ваше имя ")
    return _name


class InputError(Exception):
    """Класс ошибки"""

    def __init__(self, text):
        super(InputError, self).__init__(text)
        self.txt = text


CHOICE = {
    1: "\tHello, World",
    2: "\n\tЯ Алексей Рахманько, мне 19 лет",
    3: "\n\tМоя система - " + platform.platform(),
}
try:
    VAR = int(input("\n\tВариант (1-4): "))
    if VAR not in range(1, 5):
        raise InputError("\n\tВведите число от 1 до 4")
    if VAR == 4:
        CHOICE[4] = "\n\tДоброго времени суток, " + func()
    print(CHOICE[VAR])
except InputError as _ie:
    print(_ie)
