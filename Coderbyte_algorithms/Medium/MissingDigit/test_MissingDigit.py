'''
Unittests for MissingDigit.py
December 2020 Jakub Kazimierski
'''

import unittest
import MissingDigit

class test_MissingDigit(unittest.TestCase):    
    '''
    Class with unittests for MissingDigit.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = MissingDigit.MissingDigit("3x + 12 = 46")
        self.assertEqual(output, 4)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()