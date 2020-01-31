def good_phone(phone):
    if not phone:
        return False
    return len(phone) == 13 and phone[:4] == "+375" and phone[1:].isdigit()
