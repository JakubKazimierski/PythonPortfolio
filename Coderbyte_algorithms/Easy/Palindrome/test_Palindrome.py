'''
Unittests for Palindrome.py
October 2020 Jakub Kazimierski
'''

import unittest
import Palindrome


class test_Palindrome(unittest.TestCase):
    '''
    Class contains unittests for Palindrome.py
    '''

    #region Unittests
    def test_CorrectOutput(self):
        '''
        Checks if output is equal true when input string is palindrome.
        '''
        output = Palindrome.Palindrome("aassaa")
        self.assertEqual(output, "true")

    def test_NotPalindrome(self):
        '''
        Checks if output is equal false when input string is not a palindrome.
        '''
        output = Palindrome.Palindrome("a   assaa")
        self.assertEqual(output, "false")

    def test_UpperAndLowerCase(self):
        '''
        Checks if case of letters is ignored in comparition. 
        '''
        output = Palindrome.Palindrome("aAsSaa")
        self.assertEqual(output, "true")
    #endregion

if __name__ == "__main__":
    '''
    Main method of unittests class.
    '''
    unittest.main()        