'''
Unittests for MaxPathSumInBinaryTree.py
February 2021 Jakub Kazimierski
'''

import unittest
from MaxPathSumInBinaryTree import maxPathSum, BinaryTree

class test_MaxPathSumInBinaryTree(unittest.TestCase):    
    '''
    Class with unittests for MaxPathSumInBinaryTree.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.node_1 = BinaryTree(1)
        self.node_2 = BinaryTree(2)
        self.node_3 = BinaryTree(3)
        self.node_4 = BinaryTree(4)
        self.node_5 = BinaryTree(5)
        self.node_6 = BinaryTree(6)
        self.node_7 = BinaryTree(7)

        self.node_1.left = self.node_2
        self.node_1.right = self.node_3
        self.node_2.left = self.node_4
        self.node_2.right = self.node_5
        self.node_3.left = self.node_6
        self.node_3.right = self.node_7

        self.output = 18

        return self.node_1, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        tree, output = self.setUp()
        output_method = maxPathSum(tree)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()