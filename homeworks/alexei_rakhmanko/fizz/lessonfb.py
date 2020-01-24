"""FizzBuzz"""


def fizz():
    """Функция"""
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"
    return number


for number in range(0, 101):
    print(fizz())
