'''
Unittests for LongestMatrixPath.py
December 2020 Jakub Kazimierski
'''

import unittest
import LongestMatrixPath

class test_LongestMatrixPath(unittest.TestCase):    
    '''
    Class with unittests for LongestMatrixPath.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = LongestMatrixPath.LongestMatrixPath(["345", "326", "221"])
        self.assertEqual(output, 3)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()