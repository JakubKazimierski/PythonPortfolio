'''
Test for Alphabet Soup from coderbyte

Jakub Kazimierski 2020
'''

import unittest
import AlphabetSoup


class test_AlphabetSoup(unittest.TestCase):
    '''
    class for test unit methods
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        method check if output is sorted as expected
        '''
        output = AlphabetSoup.AlphabetSoup("ccddbbaa")
        self.assertEqual(output, "aabbccdd")

    def test_WrongInput(self):
        '''
        method check if output is correct when input is wrong
        '''
        output = AlphabetSoup.AlphabetSoup("ccd1dbbaa")
        self.assertEqual(output, -1)

    #Big letters are first before lowercase
    def test_ExpectedOutputBigLetters(self):
        '''
        check behaviour of uppercase letter
        '''
        output = AlphabetSoup.AlphabetSoup("CcdDbBaa")
        self.assertEqual(output, "BCDaabcd")

    def test_SpaceInput(self):
        '''
        check behaviour of white spaces
        '''
        output = AlphabetSoup.AlphabetSoup("ccdd bbaa")
        self.assertEqual(output, " aabbccdd")
    #endregion

if __name__ == "__main__":
    '''
    main method for tests
    '''
    unittest.main()