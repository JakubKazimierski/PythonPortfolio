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
        input_val = ["2","2","4","<>","1","1","8","<>","7","6","5"]
        output = RREF_Matrix.RREF_Matrix(input_val)
        self.assertEqual(output, "100010001")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()