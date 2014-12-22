import unittest

from stack import Stack

class StackTest(unittest.TestCase):
    
    def test_create(self):
        stack = Stack()
        self.assertEqual(stack.size, 0)

    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.size, 1)
        self.assertEqual(stack.pop(), 1)
        
    def runTest(self):
        self.test_create()
        self.test_push()    
        
unittest.main()  
    

    
