'''
Unittests for MatrixDeterminant.py
January 2021 Jakub Kazimierski
'''

import unittest
import MatrixDeterminant

class test_MatrixDeterminant(unittest.TestCase):    
    '''
    Class with unittests for MatrixDeterminant.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["1","2","4","<>","2","1","1","<>","4","1","1"]
        output = MatrixDeterminant.MatrixDeterminant(input_val)
        self.assertEqual(output, -4)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()