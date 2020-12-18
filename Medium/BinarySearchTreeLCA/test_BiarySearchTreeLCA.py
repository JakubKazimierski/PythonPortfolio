'''
Unittests for BinarySearchTreeLCA.py
December 2020 Jakub Kazimierski
'''

import unittest
import BinarySearchTreeLCA

class test_BinarySearchTreeLCA(unittest.TestCase):    
    '''
    Class with unittests for BinarySearchTreeLCA.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = BinarySearchTreeLCA.BinarySearchTreeLCA(["[10, 5, 1, 7, 40, 50]", "1", "7"])
        self.assertEqual(output, 5)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()