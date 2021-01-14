'''
Unittests for SimpleSymbols.py
from codersbyte 
October 2020 Jakub Kazimierski
'''

import unittest
import SimpleSymbols

class test_SimpleSymbols(unittest.TestCase):
    '''
    Class contains unittests for SimpleSymbols.py
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        Checks if output is true when each letter is surrounded by '+' char.
        '''
        output = SimpleSymbols.SimpleSymbols("+t+==+r+r+")
        self.assertEqual(output, "true")

    def test_LetterAtFirstIndex(self):
        '''
        Checks  if output is false if letter is at first index.
        '''
        output = SimpleSymbols.SimpleSymbols("t+==+r+r+")
        self.assertEqual(output, "false")

    def test_LetterAtLastIndex(self):
        '''
        Checks  if output is false if letter is at last index.
        '''
        output = SimpleSymbols.SimpleSymbols("+==+r+r+t")
        self.assertEqual(output, "false")

    def test_LetterNotSurrounded(self):
        '''
        Checks if output is false if letter is not surrounded by '+' char.
        '''
        output = SimpleSymbols.SimpleSymbols("+==+r+r+t=")
        self.assertEqual(output, "false")
    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()