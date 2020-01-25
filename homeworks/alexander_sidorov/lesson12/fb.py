from typing import Union

outcomes = [
    [None, "Buzz"],
    ["Fizz", "FizzBuzz"],
]


def fizzbuzz(n: int) -> Union[str, int]:
    mod3 = n % 3 == 0
    mod5 = n % 5 == 0

    outcome = outcomes[mod3][mod5] or n

    return outcome


def main():
    for i in range(101):
        fbi = fizzbuzz(i)
        print(fbi)


if __name__ == "__main__":
    main()
