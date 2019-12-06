def good_phone(number):
    return number is not None and len(number) == 13 and "+375" in number and number[1:].isdigit()
