for digit in range(0, 101):
    if digit % 3 == 0 and digit % 5 == 0:
        print("FizzBuzz")

    elif digit % 3 == 0:
        print("Fizz")

    elif digit % 5 == 0:
        print("Buzz")

    else:
        print(digit)
