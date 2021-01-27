'''
Unittests for BST_Traversal.py
January 2021 Jakub Kazimierski
'''

import unittest
from BST_Traversal import BST, inOrderTraverse, postOrderTraverse, preOrderTraverse, setUp

class test_BST_Traversal(unittest.TestCase):    
    '''
    Class with unittests for BST_Traversal.py
    '''

    # region Unittests
    def test_Inorder(self):
        '''
        Checks inorder method
        '''
        
        self.assertEqual(inOrderTraverse(setUp(), []), [2, 3, 5, 10])

    def test_Pre_Order(self):
        '''
        Checks preorder method
        '''

        self.assertEqual(preOrderTraverse(setUp(), []), [5, 2, 3, 10])

    def test_Post_Order(self):
        '''
        Checks postorder method
        '''

        self.assertEqual(postOrderTraverse(setUp(), []), [3, 2, 10, 5])

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()