'''
Unittests for SimpleSymbols.py
from codersbyte 
October 2020 Jakub Kazimierski
'''

import unittest
import SimpleSymbols

class test_SimpleSymbols(unittest.TestCase):
    '''
    class with unittests for SimpleSymbols.py
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        checks if output is true
        when each letter is surrounded by '+' char
        '''
        output = SimpleSymbols.SimpleSymbols("+t+==+r+r+")
        self.assertEqual(output, "true")

    def test_LetterAtFirstIndex(self):
        '''
        checks  if output is false
        when at first index is letter
        '''
        output = SimpleSymbols.SimpleSymbols("t+==+r+r+")
        self.assertEqual(output, "false")

    def test_LetterAtLastIndex(self):
        '''
        check if output is false 
        when letter is at last index
        '''
        output = SimpleSymbols.SimpleSymbols("+==+r+r+t")
        self.assertEqual(output, "false")

    def test_LetterNotSurrounded(self):
        '''
        check if output is false
        when letter is not surrounded by '+' char
        '''
        output = SimpleSymbols.SimpleSymbols("+==+r+r+t=")
        self.assertEqual(output, "false")
    #endregion

if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()