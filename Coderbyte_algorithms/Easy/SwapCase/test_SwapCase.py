'''
Unittests for SwapCase.py
November 2020 Jakub Kazimierski
'''

import unittest
import SwapCase

class test_SwapCase(unittest.TestCase):
    '''
    Class contains unittests for SwapCase.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if alghoritm returns expected output.
        '''
        output = SwapCase.SwapCase("aBcD")
        self.assertEqual(output, "AbCd")

    def test_LetterAndOtherCharacters(self):
        '''
        Checks if alghoritm returns expected output
        for letters and leave other signs.
        '''
        output = SwapCase.SwapCase("aB12cD?")
        self.assertEqual(output, "Ab12Cd?")

    def test_LetterAndSpaces(self):
        '''
        Checks if alghoritm returns expected output
        for letters and leave spaces.
        '''
        output = SwapCase.SwapCase(" aB cD ")
        self.assertEqual(output, " Ab Cd ")


    def test_WrongInputType(self):
        '''
        Checks if alghoritm catch exception for wrong input type.
        '''
        output = SwapCase.SwapCase(123)
        self.assertEqual(output, -1)


    #endregion

if __name__ == "__main__":
    '''
    Main method for Unittests.
    '''
    unittest.main()