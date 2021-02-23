'''
Unittests for ReconstructBST.py
February 2021 Jakub Kazimierski
'''

import unittest
from ReconstructBST import BST, reconstructBST, traversePreOrder

class test_ReconstructBST(unittest.TestCase):    
    '''
    Class with unittests for ReconstructBST.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]

        return self.preOrderTraversalValues

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr = self.setUp()
        output = reconstructBST(input_arr)

        preorder_From_Method_Output = []
        traversePreOrder(output, preorder_From_Method_Output)

        self.assertEqual(self.setUp(), preorder_From_Method_Output)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()