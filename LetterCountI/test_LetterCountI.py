'''
Unittests for LetterCountI.py
November 2020 Jakub Kazimierski
'''

import unittest
import LetterCountI

class test_LetterCountI(unittest.TestCase):
    '''
    class contains unittests for LetterCountI
    '''

    #region Unittests
    def test_WordWithMostCommonLetter(self):
        '''
        check if for word with most common letter
        output is that word
        '''
        output = LetterCountI.LetterCountI("Baranama is specific word")
        self.assertEqual(output, "Baranama")

    def test_TwoWordsSameAmountOfLetters(self):
        '''
        check if from two words with same most common amount
        of letter among all words first will be returned
        '''
        output = LetterCountI.LetterCountI("AAA BBB")
        self.assertEqual(output, "AAA")
    
    def test_SameAmountOfLetters(self):
        '''
        check if letters appear once
        output is -1
        '''
        output = LetterCountI.LetterCountI("Abc def")
        self.assertEqual(output, -1)

    def test_WrongInput(self):
        '''
        check if output is -2
        for wrong input
        '''
        output = LetterCountI.LetterCountI(-1)
        self.assertEqual(output, -2)
 
 
    #endregion

if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()