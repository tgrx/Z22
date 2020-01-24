for nmbr in range(101):
    if nmbr % 5 == 0 and nmbr % 3 == 0:
        print("FizzBuzz")
        continue
    if nmbr % 3 == 0:
        print("Fizz")

    elif nmbr % 5 == 0:
        print("Buzz")

    else:
        print(nmbr)
