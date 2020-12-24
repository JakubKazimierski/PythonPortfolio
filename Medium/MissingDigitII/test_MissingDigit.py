'''
Unittests for MissingDigitII.py
December 2020 Jakub Kazimierski
'''

import unittest
import MissingDigitII

class test_MissingDigitII(unittest.TestCase):    
    '''
    Class with unittests for MissingDigitII.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = MissingDigitII.MissingDigitII("38?5 * 3 = 1?595")
        self.assertEqual(output, "6 1")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()