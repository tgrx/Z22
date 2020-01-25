from typing import Text


def good_phone(phone: Text) -> bool:
    if not phone:
        return False

    if len(phone) != 13:
        return False

    if not phone.startswith("+375"):
        return False

    if not phone[4:].isdigit():
        return False

    return True
