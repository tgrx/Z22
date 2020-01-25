OUTCOMES = [
    [None, "Buzz"],
    ["Fizz", "FizzBuzz"],
]


def fizzbuzz(number: int) -> str:
    mod3 = number % 3 == 0
    mod5 = number % 5 == 0

    outcome = OUTCOMES[mod3][mod5]

    return outcome or str(number)


def main():
    for i in range(101):
        fbi = fizzbuzz(i)
        print(fbi)


if __name__ == "__main__":
    main()
