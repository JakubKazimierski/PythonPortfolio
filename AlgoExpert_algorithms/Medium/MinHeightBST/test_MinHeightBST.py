'''
Unittests for MinHeightBST.py
January 2021 Jakub Kazimierski
'''

import unittest
from MinHeightBST import BST, minHeightBst, preOrderTraverse

class test_MinHeightBST(unittest.TestCase):    
    '''
    Class with unittests for MinHeightBST.py
    '''

    # region Unittests
    def test_preorderOutput(self):
        '''
        Checks if preorder output is correct for builded tree.
        '''

        input_arr = [1, 2, 5, 7, 10, 13, 14, 15, 22]
        root = minHeightBst(input_arr)
        self.assertEqual(preOrderTraverse(root, []), [10, 2, 1, 5, 7, 14, 13, 15, 22])

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()