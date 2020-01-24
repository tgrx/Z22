def good_phone(phone):
    print()
    input(phone)
    if len(phone)==13:
        print(good_phone("phone"))
    else:
        print(not good_phone("phone"))