'''
Unittests for PalindromicSubstring.py
December 2020 Jakub Kazimierski
'''

import unittest
import PalindromicSubstring

class test_PalindromicSubstring(unittest.TestCase):    
    '''
    Class with unittests for PalindromicSubstring.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = PalindromicSubstring.PalindromicSubstring("abracecars")
        self.assertEqual(output, "racecar")

    def test_NoneOutput(self):
        '''
        Checks if returned output is equal 'none' if none of palindromes has length over 2.
        '''
        output = PalindromicSubstring.PalindromicSubstring("aabbcce")
        self.assertEqual(output, "none")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()