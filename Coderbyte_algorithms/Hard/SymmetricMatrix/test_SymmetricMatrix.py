'''
Unittests for SymmetricMatrix.py
January 2021 Jakub Kazimierski
'''

import unittest
import SymmetricMatrix

class test_SymmetricMatrix(unittest.TestCase):    
    '''
    Class with unittests for SymmetricMatrix.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["1","0","1","<>","0","1","0","<>","1","0","1"]
        output = SymmetricMatrix.SymmetricMatrix(input_val)
        self.assertEqual(output, "symmetric")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()