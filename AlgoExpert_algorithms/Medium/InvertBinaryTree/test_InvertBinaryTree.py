'''
Unittests for InvertBinaryTree.py
January 2021 Jakub Kazimierski
'''

import unittest
from InvertBinaryTree import BinaryTree, invertBinaryTree, preOrderTraverse

class test_InvertBinaryTree(unittest.TestCase):    
    '''
    Class with unittests for InvertBinaryTree.py
    '''

    def setUp(self):
        '''
        Sets up tree for test.
        '''
        self.tree = BinaryTree(1)
        self.tree.left = BinaryTree(2)
        self.tree.right = BinaryTree(3)
        self.tree.left.left = BinaryTree(4)
        self.tree.left.right = BinaryTree(5)
        self.tree.left.left.left = BinaryTree(8)
        self.tree.left.left.right = BinaryTree(9)
        self.tree.right.left = BinaryTree(6)
        self.tree.right.right = BinaryTree(7)

        self.inv_tree = BinaryTree(1)
        self.inv_tree.left = BinaryTree(3)
        self.inv_tree.right = BinaryTree(2)
        self.inv_tree.left.left = BinaryTree(7)
        self.inv_tree.left.right = BinaryTree(6)
        self.inv_tree.right.left = BinaryTree(5)
        self.inv_tree.right.right = BinaryTree(4)
        self.inv_tree.right.right.left = BinaryTree(9)
        self.inv_tree.right.right.right = BinaryTree(8)



    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''

        output = invertBinaryTree(self.tree)
        self.assertEqual(preOrderTraverse(output, []), preOrderTraverse(self.inv_tree, []))
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()