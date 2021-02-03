'''
Unittests for RemoveDuplicatesFromLinkedList.py
February 2021 Jakub Kazimierski
'''

import unittest
from RemoveDuplicatesFromLinkedList import LinkedList, removeDuplicatesFromLinkedList, compare_values

class test_RemoveDuplicatesFromLinkedList(unittest.TestCase):    
    '''
    Class with unittests for RemoveDuplicatesFromLinkedList.py
    '''

    def setUp(self):
        '''
        SetUp matrix for tests.
        '''
        self.begin = LinkedList(1)
        self.second = LinkedList(1)
        self.third = LinkedList(3)
        self.fourth = LinkedList(4)
        self.fifth = LinkedList(4)
        self.sixth = LinkedList(4)
        self.seventh = LinkedList(5)
        self.eighth = LinkedList(6)
        self.nineth = LinkedList(6)

        self.begin.next = self.second
        self.second.next = self.third
        self.third.next = self.fourth
        self.fourth.next = self.fifth
        self.fifth.next = self.sixth
        self.sixth.next = self.seventh
        self.seventh.next = self.eighth
        self.eighth.next = self.nineth
        
        self.out = LinkedList(1)
        self.out_2 = LinkedList(3)
        self.out_3 = LinkedList(4)
        self.out_4 = LinkedList(5)
        self.out_5 = LinkedList(6)

        self.out.next = self.out_2
        self.out_2.next = self.out_3
        self.out_3.next = self.out_4
        self.out_4.next = self.out_5
        


        return self.begin, self.out

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''

        input_l_list, no_duplicates_l_list = self.setUp()
        output = removeDuplicatesFromLinkedList(input_l_list)
        is_same = compare_values(output, no_duplicates_l_list)
        self.assertEqual(is_same, True)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()