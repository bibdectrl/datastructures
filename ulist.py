class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

    def getData(self):
        return self.elem

    def getNext(self):
        return self.next

    def setData(self, elem):
        self.elem = elem

    def setNext(self, n):
        self.next = n


class UnorderedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def add(self, elem):
        new_node = Node(elem)
        temp = self.head
        self.head = new_node
        new_node.setNext(temp)
        self._size += 1

    def isEmpty(self):
        return self.head == None

    def size(self):
        return self._size

    def search(self, target):
        if self.isEmpty():
            return False
        ptr = self.head
        while ptr.next:
            if ptr.getData() == target:
                return True
            ptr = ptr.getNext()
        return ptr.getData() == target
            
    def remove(self, target):
        current = self.head
        previous = None
        while current:
            if current.getData() == target:
                if not previous:
                    self.head = self.head.getNext()
                else:
                    previous.setNext(current.getNext())
                return
            else:
                previous = current
                current = current.getNext()

    def append(self, elem):
        current = self.head
        while current.getNext():
            current = current.getNext()
        current.setNext(Node(elem))

    def insert(self, elem, pos):
        current = self.head
        ind = 0
        while ind < pos:
            current = current.getNext()
            ind += 1
        new_node = Node(elem)
        new_node.setNext(current.getNext())
        current.setNext(new_node)    

    def index(self, i):
        current = self.head
        ind = 0
        while ind < i:
            current = current.getNext()
            ind += 1
        return current.getData()

    def pop(self, pos=0):
        if pos == 0:
            val = self.head.getData()
            self.head = self.head.getNext()
            return val
        ind = 0
        prev = None
        current = self.head
        while ind < pos:
            prev = current
            current = current.getNext()
            ind += 1
        val = current.getData()
        prev.setNext(current.getNext())
        return val

    #def pop(self, pos):
    #    pass

    def __str__(self):
        s = "[ "
        ptr = self.head
        while ptr:
            s += str(ptr.getData())
            if ptr.getNext():
                s+=", "
            ptr = ptr.getNext()
        s += " ]"
        return s


ul = UnorderedList()

[ul.add(i) for i in [3, 56, 7, "hello", 45, 23, 12, 666, 75, 2]]


print ul.head.getData()
print ul.head.getNext().getData()
print ul.head.getNext().getNext().getData()
print ul.search(666)
print ul.search(1111)

print ul
ul.remove("hello")
print ul
print ul.index(2)
ul.append("motherfucker")
ul.insert("slack", 8)
print ul
print ul.pop()
print ul
print ul.pop(1)
print ul
