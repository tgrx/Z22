N = 0

while N <= 100:
    if N % 15 == 0:
        print("FizzBuzz")
    else:
        if N % 5 == 0:
            print("Buzz")
        else:
            if N % 3 == 0:
                print("Fizz")
            else:
                print(N)
    N = N + 1
