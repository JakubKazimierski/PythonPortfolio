'''
Unittests for FindSuccessor.py
January 2021 Jakub Kazimierski
'''

import unittest
from FindSuccessor import BinaryTree, findSuccessor

class test_FindSuccessor(unittest.TestCase):    
    '''
    Class with unittests for FindSuccessor.py
    '''

    def setUp(self):
        '''
        Sets up tree for test.
        I hate this one but this is still a test.
        Insert method was not implemented for this task.
        '''
        # define nodes
        self.root = BinaryTree(1)
        self.child_left = BinaryTree(2)
        self.child_right = BinaryTree(3)
        self.child_left_left = BinaryTree(4)
        self.child_left_right = BinaryTree(5)
        self.child_left_left_left = BinaryTree(6)

        # define connections
        self.root.left = self.child_left
        self.root.right = self.child_right
        self.child_left.parent = self.root
        self.child_right.parent = self.root

        self.child_left.left = self.child_left_left
        self.child_left.right = self.child_left_right
        self.child_left_left.parent = self.child_left
        self.child_left_right.parent = self.child_left

        self.child_left_left.left = self.child_left_left_left
        self.child_left_left_left.parent = self.child_left_left




    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_node = self.child_left_right
        output = findSuccessor(self.root, input_node)
        self.assertEqual(output, self.root)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()