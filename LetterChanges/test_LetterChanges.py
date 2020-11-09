'''
Unittests for LetterChanges from codersbyte
October 2020 Jakub Kazimierski
'''

import unittest
import LetterChanges


class test_LetterChanges(unittest.TestCase):
    '''
    class with unittests for Letter Changes
    '''

    #region Unittests    
    def test_ProperOutput(self):
        '''
        check for expected output
        '''
        output = LetterChanges.LetterChanges("aaa bbb ccc")
        self.assertEqual(output, "bbb ccc ddd")

    def test_ProperOutputVowels(self):
        '''
        check if vowels became uppercase
        '''
        output = LetterChanges.LetterChanges("bbb ccc ddd")
        self.assertEqual(output, "ccc ddd EEE")

    def test_EmptyOutput(self):
        '''
        check output for empty input
        '''
        output = LetterChanges.LetterChanges("")
        self.assertEqual(output, "")

    def test_NoLetters(self):
        '''
        check if input without letters
        is the same at output
        '''
        output = LetterChanges.LetterChanges("1234")
        self.assertEqual(output, "1234")

    def test_MixedLettersOtherSignsOutput(self):
        '''
        check if output is as expected
        for mixed characters
        '''
        output = LetterChanges.LetterChanges("1234a?//")
        self.assertEqual(output, "1234b?//")
    #endregion

if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()        