'''
Unitests for WordCount.py from codersbyte
October 2020 Jakub Kazimierski
'''

import unittest
import WordCount

class test_WordCount(unittest.TestCase):
    '''
    class with unittests for WordCount.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        check if output is as expected
        '''
        output = WordCount.WordCount("Aaaa sff ewq")
        self.assertEqual(output, 3)

    def test_LettersAndNumbers(self):
        '''
        check if numerics characters
        are counted as words
        '''
        output = WordCount.WordCount("Aaaa 1 2")
        self.assertEqual(output, 3)

    def test_LettersAndVariousChars(self):
        '''
        check if non alphabeticals characters
        are counted as words
        '''
        output = WordCount.WordCount("Aaaa #@@ ></]")
        self.assertEqual(output, 3)

    def test_OneWord(self):
        '''
        check if one word at input is counted properly
        '''
        output = WordCount.WordCount("#@@></]")
        self.assertEqual(output, 1)

    def test_EmptyInput(self):
        '''
        check if empty input returns '0'
        '''
        output = WordCount.WordCount("")
        self.assertEqual(output, 0)

    def test_WrongTypeInput(self):
        '''
        check if wrong type input
        returns value '-1'
        '''
        output = WordCount.WordCount(False)
        self.assertEqual(output, -1)
    #endregion

if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()