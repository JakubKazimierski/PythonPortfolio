'''
Unittests for Palindrome.py
October 2020 Jakub Kazimierski
'''

import unittest
import Palindrome


class test_Palindrome(unittest.TestCase):
    '''
    class with unittests for Palindrome.py
    '''

    #region Unittests
    def test_CorrectOutput(self):
        '''
        check if output is true when input string
        is palindrome
        '''
        output = Palindrome.Palindrome("aassaa")
        self.assertEqual(output, "true")

    def test_CorrectOutputMeanLetters(self):
        '''
        check if space characters make true output still valid
        '''
        output = Palindrome.Palindrome("a   assaa")
        self.assertEqual(output, "true")

    def test_IncorrectSignsInInput(self):
        '''
        check if output is -1 when in string are other signs
        than alphabetical and spaces
        '''
        output = Palindrome.Palindrome("aa2ss2aa")
        self.assertEqual(output, -1)

    def test_UpperAndLowerCase(self):
        '''
        check if output is true when in input string
        are uppercase and lowercase mixed
        '''
        output = Palindrome.Palindrome("aAsSaa")
        self.assertEqual(output, "true")
    #endregion

if __name__ == "__main__":
    '''
    main method of unittests class
    '''
    unittest.main()        