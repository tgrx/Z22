 

def enqueue(fifo, elm):
    
    fifo.insert(0,elm)
    
    


def dequeue(fifo):
    if fifo == [""]:
        return None
    return fifo.pop()
