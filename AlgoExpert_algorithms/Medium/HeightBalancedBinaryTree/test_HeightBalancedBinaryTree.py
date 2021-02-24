'''
Unittests for HeightBalancedBinaryTree.py
February 2021 Jakub Kazimierski
'''

import unittest
from HeightBalancedBinaryTree import BinaryTree, heightBalancedBinaryTree

class test_HeightBalancedBinaryTree(unittest.TestCase):    
    '''
    Class with unittests for HeightBalancedBinaryTree.py
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
        self.node_8 = BinaryTree(8)

        self.node_1.left = self.node_2
        self.node_1.right = self.node_3
        self.node_2.left = self.node_4
        self.node_2.right = self.node_5
        self.node_5.left = self.node_7
        self.node_5.right = self.node_8
        self.node_3.right = self.node_6

        return self.node_1, True

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        Input cannot be empty string.
        '''
        root, output = self.setUp()
        output_bool = heightBalancedBinaryTree(root)

        self.assertEqual(output, output_bool)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()