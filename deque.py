import string

class Deque:
    def __init__(self):
        self._elems = []
        self._size = 0

    def addFront(self, n):
        self._elems.insert(0, n)
        self._size += 1

    def addRear(self, n):
        self._elems.append(n)
        self._size += 1

    def removeFront(self):
        self._size -= 1
        return self._elems.pop(0)

    def removeRear(self):
        self._size -= 1
        return self._elems.pop()

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self._size



def palindrome_check(word):
    alpha = string.lowercase
    d = Deque()
    for char in word:
        if char in alpha:
            d.addRear(char)
    while d.size() > 1:
        if d.removeFront() != d.removeRear():
            return False
    return True


print palindrome_check("a man, a plan, a canal, panama")
print palindrome_check("sdfsdfsdfsdfsaaer")
