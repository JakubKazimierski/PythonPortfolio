'''
Unittests for FindNodesDistanceK.py
February 2021 Jakub Kazimierski
'''


import unittest
from FindNodesDistanceK import findNodesDistanceK, BinaryTree

class test_FindNodesDistanceK(unittest.TestCase):    
    '''
    Class with unittests for FindNodesDistanceK.py
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
        self.node_3.right = self.node_6
        self.node_6.left = self.node_7
        self.node_6.right = self.node_8

        self.output = [2, 7, 8]
        self.target = 3
        self.k = 2
        return self.node_1, self.target, self.k, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        tree, target, k, output = self.setUp()
        output_method = findNodesDistanceK(tree, target, k)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()