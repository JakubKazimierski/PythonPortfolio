'''
Unittests for LogitRegression.py
January 2021 Jakub Kazimierski
'''

import unittest
import LogitRegression

class test_LogitRegression(unittest.TestCase):    
    '''
    Class with unittests for LogitRegression.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = LogitRegression.LogitRegression([1, 1, 1, 1])
        self.assertEqual(output, "0.881, 0.881")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()