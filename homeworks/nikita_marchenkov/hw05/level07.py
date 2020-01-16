from homeworks.nikita_marchenkov.hw05 import level06


def enqueue(dictionary, priority, element):
    scroll = dictionary.setdefault(priority, [])
    level06.enqueue(scroll, element)


def dequeue(dictionary):
    if not dictionary:
        return None
    result = dictionary.get(max(dictionary))[0]
    del dictionary.get(max(dictionary))[0]
    if not dictionary.get(max(dictionary)):
        del dictionary[max(dictionary)]
    return result
