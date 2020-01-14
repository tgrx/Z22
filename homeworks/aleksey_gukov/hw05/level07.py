def enqueue(dictionary, priority, element):
    lst = dictionary.setdefault(priority, [])
    lst.append(element)


def dequeue(dictionary):
    if not dictionary:
        return None
    maxkey = max(list(dictionary.keys()))
    lst = dictionary.get(maxkey)
    answer = dictionary.get(maxkey)[0]
    del dictionary.get(maxkey)[0]
    if len(lst) == 0:
        del dictionary[maxkey]
    return answer
