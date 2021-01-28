'''
Unittests for BinaryTreeDiameter.py
January 2021 Jakub Kazimierski
'''

import unittest
from BinaryTreeDiameter import BinaryTree, binaryTreeDiameter

class test_BinaryTreeDiameter(unittest.TestCase):    
    '''
    Class with unittests for BinaryTreeDiameter.py
    '''

    def setUp(self):
        '''
        Sets up tree for test.
        '''
        self.tree = BinaryTree(1)
        self.tree.left = BinaryTree(3)
        self.tree.right = BinaryTree(2)
        self.tree.left.left = BinaryTree(7)
        self.tree.left.right = BinaryTree(4)
        self.tree.left.left.left = BinaryTree(8)
        self.tree.left.left.left.left = BinaryTree(9)
        self.tree.left.right.right = BinaryTree(5)
        self.tree.left.right.right.right = BinaryTree(6)


    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''

        output = binaryTreeDiameter(self.tree)
        self.assertEqual(output, 6)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()