'''
Unittests for FindKthLargestValueInBST.py
February 2021 Jakub Kazimierski
'''


import unittest
from FindKthLargestValueInBST import BST, findKthLargestValueInBST

class test_FindKthLargestValueInBST(unittest.TestCase):    
    '''
    Class with unittests for FindKthLargestValueInBST.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''
        self.node_1 = BST(15)
        self.node_2 = BST(5)
        self.node_3 = BST(20)
        self.node_4 = BST(2)
        self.node_5 = BST(5)
        self.node_6 = BST(17)
        self.node_7 = BST(22)
        self.node_8 = BST(1)
        self.node_I = BST(3)

        self.k = 3

        self.node_1.left = self.node_2
        self.node_1.right = self.node_3
        self.node_2.left = self.node_4
        self.node_2.right = self.node_5
        self.node_3.left = self.node_6
        self.node_3.right = self.node_7
        self.node_4.left = self.node_8
        self.node_4.right = self.node_3

        self.output = 17

        return self.node_1, self.k, self.output

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_tree, input_k, proper_out  = self.setUp()
        output = findKthLargestValueInBST(input_tree, input_k)
        self.assertEqual(output, proper_out)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()