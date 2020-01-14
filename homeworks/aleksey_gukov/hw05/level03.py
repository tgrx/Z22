def good_phone(number):
    if not number:
        return False
    return number[:4] == "+375" and len(number) == 13 and number[1:].isdigit()
