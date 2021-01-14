'''
Unittests for RomanNumeralReduction.py
January 2021 Jakub Kazimierski
'''

import unittest
import RomanNumeralReduction

class test_RomanNumeralReduction(unittest.TestCase):    
    '''
    Class with unittests for RomanNumeralReduction.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = RomanNumeralReduction.RomanNumeralReduction("LLLXXXVVVV")
        self.assertEqual(output, 'CC')

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()