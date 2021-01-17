'''
Unittests for PentagonalNumber.py
January 2021 Jakub Kazimierski
'''

import unittest
import PentagonalNumber

class test_PentagonalNumber(unittest.TestCase):    
    '''
    Class with unittests for PentagonalNumber.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = PentagonalNumber.PentagonalNumber(5)
        self.assertEqual(output, 51)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()