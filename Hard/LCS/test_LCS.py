'''
Unittests for LCS.py
January 2021 Jakub Kazimierski
'''

import unittest
import LCS

class test_LCS(unittest.TestCase):    
    '''
    Class with unittests for LCS.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = LCS.LCS(["abcabb","bacb"])
        self.assertEqual(output, 3)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()