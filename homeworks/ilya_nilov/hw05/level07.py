from collections import OrderedDict


def enqueue(line, priority, content):
    line[priority] = OrderedDict.move_to_end(content, last=True)
    

  
    


def dequeue(line):
    if not line:
        return None
    for key in line:


    return line.


