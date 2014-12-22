class Stack:
    def __init__(self):
        self.elems = []
        self.size = 0

    def push(self, x):
        self.elems.append(x)
        self.size += 1
				
    def pop(self):
        return self.elems.pop()
        #last = self.elems[-1]
        #del self.elems[-1]
        #self.size -= 1
        #return last
	
    def peek(self):
        last = self.elems[-1]
        return last
		
    def isEmpty(self):
        return self.size == 0
		
    def size(self):
        return self.size
