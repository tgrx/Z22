for chislo in range(0, 101):
    if chislo % 3 == 0 and chislo % 5 == 0:
        print("FizzBuzz")
    elif chislo % 3 == 0:
        print("Fizz")
    elif chislo % 5 == 0:
        print("Buzz")
    else:
        print(chislo)
