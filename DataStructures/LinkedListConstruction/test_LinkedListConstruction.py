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

        self.list = DoublyLinkedList()
        self.list.setHead(self.one)
        self.list.insertAfter(self.one, self.two)
        self.list.insertBefore(self.one, self.three)
        self.list.setTail(self.four)
        self.list.remove(self.four)
        self.list.setTail(self.five)
        
        
        return self.list

    # region Unittests
    def test_head(self):   
        '''
        Checks if head is correct.
        That means that insert before is also correct.
        '''
        proper_list = self.SetUp()
        self.assertEqual(proper_list.head.value, 3)

    def test_tail(self):   
        '''
        Checks if tail is correct.
        That means that insert after is also correct.
        '''
        proper_list = self.SetUp()
        self.assertEqual(proper_list.tail.value, 5)

    def test_removal(self):   
        '''
        Checks if remove method is correct.
        That means that contains() method also is correct.
        '''
        proper_list = self.SetUp()
        is_four = proper_list.containsNodeWithValue(4)
        self.assertEqual(is_four, False)



    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()