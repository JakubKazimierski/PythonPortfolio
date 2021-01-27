'''
Unittests for FindClosestValueInBST.py
January 2021 Jakub Kazimierski
'''

import unittest
from FindClosestValueInBST import findClosestValueInBst, BST, setUp

class test_FindClosestValueInBST(unittest.TestCase):    
    '''
    Class with unittests for FindClosestValueInBST.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        
        root = setUp()
        
        input_target  = 12        
        output = findClosestValueInBst(root, input_target)
        self.assertEqual(output, 13)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()