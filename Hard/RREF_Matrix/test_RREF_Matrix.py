'''
Unittests for RREF_Matrix.py
January 2021 Jakub Kazimierski
'''

import unittest
import RREF_Matrix

class test_RREF_Matrix(unittest.TestCase):    
    '''
    Class with unittests for RREF_Matrix.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["5","7","8","<>","1","1","2"]
        output = RREF_Matrix.RREF_Matrix(input_val)
        self.assertEqual(output, "D-B-A-F")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()