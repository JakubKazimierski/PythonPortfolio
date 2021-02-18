'''
Unittests for SumOfLinkedList.py
February 2021 Jakub Kazimierski
'''


import unittest
from SumOfLinkedList import LinkedList, sumOfLinkedLists, checkValues

class test_SumOfLinkedList(unittest.TestCase):    
    '''
    Class with unittests for SumOfLinkedList.py
    '''

    def setUp(self):
        '''
        Sets up input and output.
        '''
        self.rootOne = LinkedList(2)
        self.rootOne.next = LinkedList(4)
        self.rootOne.next.next = LinkedList(7)
        self.rootOne.next.next.next = LinkedList(1)

        self.rootTwo  = LinkedList(9)
        self.rootTwo.next = LinkedList(4)
        self.rootTwo.next.next = LinkedList(5)

        self.outputRoot = LinkedList(1)
        self.outputRoot.next = LinkedList(9)
        self.outputRoot.next.next = LinkedList(2)
        self.outputRoot.next.next.next = LinkedList(2)

        return self.rootOne, self.rootTwo, self.outputRoot
    
    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        ListOne, ListTwo, outputList = self.setUp()
        method_output = sumOfLinkedLists(ListOne, ListTwo)

        are_same = checkValues(outputList, method_output)

        self.assertEqual(True, are_same)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()