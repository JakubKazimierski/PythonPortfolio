'''
Unittestst for OffBinary.py
December 2020 Jakub Kazimierski
'''

import unittest
import OffBinary

class test_OffBinary(unittest.TestCase):    
    '''
    Class with unittests for OffBinary.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = OffBinary.OffBinary(["56", "011000"] )
        self.assertEqual(output, 1)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()