'''
Unittests for RemoveKthNodeFromEnd.py
February 2021 Jakub Kazimierski
'''

import unittest
from RemoveKthNodeFromEnd import removeKthNodeFromEnd, LinkedList, returnValues

class test_RemoveKthNodeFromEnd(unittest.TestCase):    
    '''
    Class with unittests for RemoveKthNodeFromEnd.py
    '''

    def SetUp(self):
        '''
        Set Up input list.
        '''
        
        self.zero = LinkedList(0)
        self.one = LinkedList(1)
        self.two = LinkedList(2)
        self.three = LinkedList(3)
        self.four = LinkedList(4)
        self.five = LinkedList(5)
        self.six = LinkedList(6)
        self.seven = LinkedList(7)
        self.eight = LinkedList(8)
        self.nine = LinkedList(9)
        
        self.zero.next = self.one
        self.one.next = self.two
        self.two.next = self.three
        self.three.next = self.four
        self.four.next = self.five
        self.five.next = self.six
        self.six.next = self.seven
        self.seven.next = self.eight
        self.eight.next = self.nine

        self.k = 4

        return self.zero, self.k

    # region Unittests
    def test_RemoveKthNodeFromEnd(self):   
        '''
        Checks if output is correct.
        '''
        head, k = self.SetUp()
        # call method
        removeKthNodeFromEnd(head, k)
        output_values = [0, 1, 2, 3, 4, 5, 7, 8, 9]
        self.assertEqual(returnValues(head), output_values)


    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()