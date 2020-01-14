def good_phone(number):
    number = str(number)
    return number[1:].isdigit() and "+375" in number and len(number) == 13
