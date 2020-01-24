def good_phone(phone_numbers):
    """ Good_phone function"""

    phone_number = str(phone_numbers)
    if phone_number[1:].isdigit() and phone_number.startswith("+375"):
        return len(phone_number) == 13

    else:
        return False
