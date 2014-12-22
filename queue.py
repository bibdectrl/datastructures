class Queue:
    def __init__(self):
        self.elems = []

    def enqueue(self, n):
        self.elems = [n] + self.elems
        
    def dequeue(self):
        return self.elems.pop()

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.elems)
