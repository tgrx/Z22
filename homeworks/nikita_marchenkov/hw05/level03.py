def good_phone(number):
    if not number:
        return False
    return (
        number
        and len(number) == 13
        and number[0:4] == "+375"
        and set(number[1:13]).issubset(set("0123456789"))
    )
