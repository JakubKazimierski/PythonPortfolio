'''
Unittests for LetterCountI from Coderbyte
November 2020 Jakub Kazimierski
'''

import unittest
import LetterCountI_Improved

class test_LetterCountI(unittest.TestCase):
    '''
    Class contains unittests for LetterCountI.py
    '''

    #region Unittests
    def test_WordWithMostCommonLetter(self):
        '''
        Checks if for word with most common letter output is that word.
        '''
        output = LetterCountI_Improved.LetterCountI("Baranama is specific word")
        self.assertEqual(output, "Baranama")

    def test_TwoWordsSameAmountOfLetters(self):
        '''
        Checks if for two words having same amount of most common letter 
        first word appearing in string will be returned.
        '''
        output = LetterCountI_Improved.LetterCountI("AAA BBB")
        self.assertEqual(output, "AAA")
    
    def test_SameAmountOfLetters(self):
        '''
        Checks if output is equal -1 if
        each letter appear once in word.
        '''
        output = LetterCountI_Improved.LetterCountI("Abc def")
        self.assertEqual(output, -1)

    def test_WrongInput(self):
        '''
        Checks if output is equal -2
        for wrong input type.
        '''
        output = LetterCountI_Improved.LetterCountI(-1)
        self.assertEqual(output, -2)
 
 
    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()