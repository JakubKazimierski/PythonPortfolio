'''
Unittests for LetterCapitalize
October 2020 Jakub Kazimierski
'''

import unittest
import LetterCapitalize

class test_LetterCapitalize(unittest.TestCase):
    '''
    Class contains unittests for LetterCapitalize.py
    '''
    #region Unittests
    def test_ProperOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = LetterCapitalize.LetterCapitalize("so it's begin")
        self.assertEqual(output, "So It's Begin")

    def test_OutputWithNumbers(self):
        '''
        Checks if numbers in words affect proper output.
        '''
        output = LetterCapitalize.LetterCapitalize("3llo fr1end")
        self.assertEqual(output, "3llo Fr1end")

    def test_OutputWithCapitals(self):
        '''
        Checks if capital letters already are in string 
        then output is the same.
        '''
        output = LetterCapitalize.LetterCapitalize("So It's Begin")
        self.assertEqual(output, "So It's Begin")

    #for this task only first letters has to be Capital in output
    def test_CapitalsInTheMiddle(self):
        '''
        Checks if uppercase letters are not te first ones in words
        then each one of them becomes lowercase.
        '''
        output = LetterCapitalize.LetterCapitalize("sO it'S beGin")
        self.assertEqual(output, "So It's Begin")
    #endregion


if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()