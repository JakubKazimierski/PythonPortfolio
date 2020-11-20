'''
Unittests for LongestWord from Coderbyte
October 2020 Jakub Kazimierski
'''

import unittest
import LongestWord

class test_LongestWord(unittest.TestCase):
    '''
    Class contains unittests for LongestWord.py
    '''

    #region Unittests       
    def test_ProperOutput(self):
        '''
        Checks if output is as expected.
        '''
        output  = LongestWord.LongestWord("Aaaaa bbbb ccc")
        self.assertEqual(output, "Aaaaa")

    def test_SecondLongestWord(self):
        '''
        Checks if output is not equal to second longest word.
        '''
        output  = LongestWord.LongestWord("Aaaaa bbbbb ccc")
        self.assertNotEqual(output, "bbbbb")

    def test_ProperOutput3(self):
        '''
        Checks if numbers are count as word.
        '''
        output  = LongestWord.LongestWord("bbbb ccc1234ddddd")
        self.assertEqual(output, "ccc1234ddddd")

    def test_EmptyInput(self):
        '''
        Checks if output is equal -1 for empty input.
        '''
        output = LongestWord.LongestWord("")
        self.assertEqual(output, -1)

    def test_PunctuationInInput(self):
        '''
        Checks if output is equal -1 for punctuation in input.
        '''
        output = LongestWord.LongestWord("asd, ff")
        self.assertEqual(output, -1)    
    #endregion
            
if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()        