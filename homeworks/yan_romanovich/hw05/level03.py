def good_phone(number):
    if number is not None:
        return len(number) == 13 and "+375" in number and number[1:].isdigit()
    return False
