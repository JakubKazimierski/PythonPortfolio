'''
Unittests for BST_Construction.py
January 2021 Jakub Kazimierski
'''

import unittest
from BST_Construction import BST

class test_BST_Construction(unittest.TestCase):    
    '''
    Class with unittests for BST_Construction.py
    '''

    # region Unittests
    def test_Insert(self):
        '''
        Checks insertion method
        '''
        root = BST(5)
        root.insert(10)
        root.insert(2)
        root.insert(3)

        self.assertEqual(root.left.value, 2)
        self.assertEqual(root.right.value, 10)
        self.assertEqual(root.left.right.value, 3)
        self.assertEqual(root.value, 5)

    def test_Delete(self):
        '''
        Checks deletion method
        '''
        root = BST(5)
        root.insert(10)
        root.insert(2)
        root.insert(3)
        root.remove(2)

        self.assertEqual(root.left.value, 3)
        self.assertEqual(root.right.value, 10)
        self.assertEqual(root.left.right, None)
        self.assertEqual(root.left.left, None)
   
    def test_Contains(self):
        '''
        Checks conatins method
        '''
        root = BST(5)
        root.insert(10)
        root.insert(2)
        root.insert(3)
        root.remove(2)

        self.assertEqual(root.contains(2), False)
        self.assertEqual(root.contains(10), True)
        self.assertEqual(root.contains(3), True)
        self.assertEqual(root.contains(5), True)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()