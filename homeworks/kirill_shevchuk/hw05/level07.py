from homeworks.kirill_shevchuk.hw05 import level06


def enqueue(dictionary, priority, element):
    """ добавляет элемент e в конец очереди l с приоритетом p """
    line = dictionary.setdefault(priority, [])
    level06.enqueue(line, element)


def dequeue(dictionary):
    """
    вынимает элемент из начала очереди и возвращает его
    если очередь пуста - возвращается None
    элементы возвращаются согласно приоритету
    """
    if not dictionary:
        return None
    if not dictionary.get(max(dictionary.keys())):
        del dictionary[max(dictionary.keys())]
    return (
        None
        if not dictionary
        else level06.dequeue(dictionary.get(max(dictionary.keys())))
    )
