'''
Unittests for ValidateBST.py
January 2021 Jakub Kazimierski
'''

import unittest
from ValidateBST import BST, validateBst, setUp

class test_ValidateBST(unittest.TestCase):    
    '''
    Class with unittests for ValidateBST.py
    '''
    
    # region Unittests
    def test_Insert(self):
        '''
        Checks insertion method
        '''
        root = setUp()

        self.assertEqual(root.left.value, 2)
        self.assertEqual(root.right.value, 10)
        self.assertEqual(root.left.right.value, 3)
        self.assertEqual(root.value, 5)

    def test_Validation(self):
        '''
        Checks deletion method
        '''
        root = setUp()
        self.assertEqual(validateBst(root), True)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()