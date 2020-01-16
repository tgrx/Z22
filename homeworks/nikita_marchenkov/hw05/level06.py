def enqueue(self, data):
    return self.append(data)


def dequeue(self):
    if self:
        return self.pop(0)
    return None
