'''
Unittests for BranchSums.py
January 2021 Jakub Kazimierski
'''

import unittest
import BranchSums
from BranchSums import BinaryTree

class test_BranchSums(unittest.TestCase):    
    '''
    Class with unittests for BranchSums.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''

        # below creates linked Binary Tree        
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(9)
        root.left.right.left = BinaryTree(10)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        
        output = BranchSums.branchSums(root)
        self.assertEqual(output, [15, 16, 18, 10, 11])
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()