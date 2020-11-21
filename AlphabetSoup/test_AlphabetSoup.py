'''
Class contains unittests for AlphabetSoup.py
Jakub Kazimierski October 2020
'''

import unittest
import AlphabetSoup

class test_AlphabetSoup(unittest.TestCase):
    '''
    Class contains unittests for AlphabetSoup.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is sorted in alphabetical order.
        '''
        output = AlphabetSoup.AlphabetSoup("ccddbbaa")
        self.assertEqual(output, "aabbccdd")

    def test_WrongInput(self):
        '''
        Checks if output is -1 when input is wrong type.
        '''
        output = AlphabetSoup.AlphabetSoup(112)
        self.assertEqual(output, -1)

    #Big letters are first before lowercase
    def test_ExpectedOutputBigLetters(self):
        '''
        Checks if uppercase letters are sorted before lowercase letters.
        '''
        output = AlphabetSoup.AlphabetSoup("CcdDbBaa")
        self.assertEqual(output, "BCDaabcd")

    def test_SpaceInput(self):
        '''
        Check if whitespaces are sorted before letters.
        '''
        output = AlphabetSoup.AlphabetSoup("ccdd bbAa")
        self.assertEqual(output, " Aabbccdd")
    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests' Class.
    '''
    unittest.main()