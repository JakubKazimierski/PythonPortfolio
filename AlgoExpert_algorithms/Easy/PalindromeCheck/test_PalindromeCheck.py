'''
Unittests for PalindromeCheck.py
January 2021 Jakub Kazimierski
'''

import unittest
import PalindromeCheck

class test_PalindromeCheck(unittest.TestCase):    
    '''
    Class with unittests for PalindromeCheck.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_str  = "abcdcba"
        output = PalindromeCheck.palindromeCheck(input_str)
        self.assertEqual(output, True)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()