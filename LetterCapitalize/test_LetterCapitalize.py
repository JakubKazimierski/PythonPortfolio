'''
Unittests for LetterCapitalize
October 2020 Jakub Kazimierski
'''

import unittest
import LetterCapitalize

class test_LetterCapitalize(unittest.TestCase):
    '''
    class contains unittests for LetterCapitalize method
    '''
    #region Unittests
    def test_ProperOutput(self):
        '''
        Check if output is as expected
        '''
        output = LetterCapitalize.LetterCapitalize("so it's begin")
        self.assertEqual(output, "So It's Begin")

    def test_OutputWithNumbers(self):
        '''
        check if numbers affect proper output
        '''
        output = LetterCapitalize.LetterCapitalize("h3llo fr1end")
        self.assertEqual(output, "H3llo Fr1end")

    def test_OutputWithCapitals(self):
        '''
        Capital letters already are in string 
        so output should be the same
        '''
        output = LetterCapitalize.LetterCapitalize("So It's Begin")
        self.assertEqual(output, "So It's Begin")

    #for this task only forst letters has to be Capital in output
    def test_CapitalsInTheMiddle(self):
        '''
        if uppercase letters are not te first ones of word
        each one of them should became lowercase
        '''
        output = LetterCapitalize.LetterCapitalize("sO it'S beGin")
        self.assertEqual(output, "So It's Begin")
    #endregion


if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()