'''
Unittests for FindClosestValueInBST.py
January 2021 Jakub Kazimierski
'''

import unittest
import FindClosestValueInBST
from FindClosestValueInBST import insert
from FindClosestValueInBST import BST

class test_FindClosestValueInBST(unittest.TestCase):    
    '''
    Class with unittests for FindClosestValueInBST.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        
        root = BST(10)
        root = insert(root, 5)
        root = insert(root, 15)
        root = insert(root, 2)
        root = insert(root, 5)
        root = insert(root, 1)
        root = insert(root, 22)
        root = insert(root, 13)
        root = insert(root, 14)

        
        input_target  = 12        
        output = FindClosestValueInBST.findClosestValueInBst(root, input_target)
        self.assertEqual(output, 13)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()