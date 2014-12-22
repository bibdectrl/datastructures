import unittest

from olist import OrderedList

class OlistTest(unittest.TestCase):


    def test_create(self):
        o = OrderedList()
        self.assertEqual(o._size, 0)
    
    def test_add(self):
        o = OrderedList()
        o.add(0)
        o.add(1)
        o.add(2)
        o.add(3)
        o.add(4)
        self.assertEqual(o._size, 5)



unittest.main()


