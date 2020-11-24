'''
Unittests for MinWindowSubstring from Coderbyte
October 2020 Jakub Kazimierski
'''

import unittest
import MinWindowSubstring


class test_MinWindowSubstring(unittest.TestCase):
    '''
    Class contains unittests fro MinWindowSubstring.py
    '''

    #region Unittests
    def test_ValidOutput(self):
        '''
        Checks if output is as expeted.
        '''
        output = MinWindowSubstring.MinWindowSubstring(["aaabaaddae", "aed"])
        self.assertEqual(output, "dae")

    def test_NotValidOutput(self):
        '''
        Checks if output is false when is no common substring.
        '''
        output = MinWindowSubstring.MinWindowSubstring(["aaabaadda", "aed"])
        self.assertEqual(output, False)

    def test_SameSymbolsNotSameCount(self):
        '''
        Checks if output is false when occurance of same symbols is at least not the same
        in both strings.
        '''
        output = MinWindowSubstring.MinWindowSubstring(["aaddef", "aaeedd"])
        self.assertEqual(output, False)

    def test_SecondStringIsEmptyInput(self):
        '''
        Checks if output is false if second string is empty.
        '''
        output = MinWindowSubstring.MinWindowSubstring(["aaddef", ""])
        self.assertEqual(output, False)

    def test_FirstStringIsEmptyInput(self):
        '''
        Checks if output is false when first string is empty.
        '''
        output = MinWindowSubstring.MinWindowSubstring(["", "ass"])
        self.assertEqual(output, False)

    def test_BothStringsAreEmpty(self):
        '''
        Checks if output is false if both strings are empty.
        '''
        output = MinWindowSubstring.MinWindowSubstring(["", ""])
        self.assertEqual(output, False)    
    #endregion
    
if __name__ == "__main__":
    '''
    Main method of unittests class.
    '''
    unittest.main()        