'''
Unittests for LinkedListConstruction.py
February 2021 Jakub Kazimierski
'''

import unittest
from LinkedListConstruction import Node, DoublyLinkedList

class test_LinkedListConstruction(unittest.TestCase):    
    '''
    Class with unittests for LinkedListConstruction.py
    '''

    def SetUp(self):
        '''
        Set Up input list.
        '''
        
        self.one = Node(1)
        self.two = Node(2)
        self.three = Node(3)
        self.four = Node(4)
        self.five = Node(5)

        self.one.next = self.two
        self.two.prev = self.one
        self.two.next = self.three
        self.three.prev = self.two
        self.three.next = self.four
        self.four.prev = self.three
        self.four.next = self.five
        self.five.prev = self.four


        return self.one

    # region Unittests
    def test_buildHeap(self):   
        '''
        Checks if Heap is built correctly.
        '''
#        proper_list = self.SetUp()



    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()