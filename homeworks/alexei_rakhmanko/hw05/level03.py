"""Уровень 3"""


def good_phone(tel):
    """Функция"""
    return tel and len(tel) == 13 and tel[:4] == "+375" and tel[1:].isdigit()
