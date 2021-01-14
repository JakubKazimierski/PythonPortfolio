'''
Unitests for WordCount.py
October 2020 Jakub Kazimierski
'''

import unittest
import WordCount

class test_WordCount(unittest.TestCase):
    '''
    Class contains unittests for WordCount.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = WordCount.WordCount("Aaaa sff ewq")
        self.assertEqual(output, 3)

    def test_LettersAndNumbers(self):
        '''
        Checks if numerics characters are counted as words.
        '''
        output = WordCount.WordCount("Aaaa 1 2")
        self.assertEqual(output, 3)

    def test_LettersAndVariousChars(self):
        '''
        Checks if non alphabeticals characters are counted as words.
        '''
        output = WordCount.WordCount("Aaaa #@@ ></]")
        self.assertEqual(output, 3)

    def test_OneWord(self):
        '''
        Checks if one word at input is counted properly.
        '''
        output = WordCount.WordCount("#@@></]")
        self.assertEqual(output, 1)

    def test_EmptyInput(self):
        '''
        Checks if for empty input output is '0'.
        '''
        output = WordCount.WordCount("")
        self.assertEqual(output, 0)

    def test_WrongTypeInput(self):
        '''
        Checks if for wrong type of input, output is '-1'.
        '''
        output = WordCount.WordCount(False)
        self.assertEqual(output, -1)
    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()