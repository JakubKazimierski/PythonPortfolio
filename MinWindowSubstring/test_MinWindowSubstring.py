'''
Unittests for MinWindowSubstring from codersbyte
October 2020 Jakub Kazimierski
'''

import unittest
import MinWindowSubstring


class test_MinWindowSubstring(unittest.TestCase):
    '''
    class contains unittests fro MinWindowSubstring from codersbyte
    '''

    #region Unittests
    def test_ValidOutputLength(self):
        '''
        check if output is as expeted
        '''
        output = MinWindowSubstring.MinWindowSubstring(["aaabaaddae", "aed"])
        self.assertEqual(output, "dae")

    def test_NotValidOutput(self):
        '''
        check if output is false when is no common substring
        '''
        output = MinWindowSubstring.MinWindowSubstring(["aaabaadda", "aed"])
        self.assertEqual(output, False)

    def test_SameSymbolsNotSameCount(self):
        '''
        check if output is false when number of symbols is not the same
        in strings
        '''
        output = MinWindowSubstring.MinWindowSubstring(["aaddef", "aaeedd"])
        self.assertEqual(output, False)

    def test_NotValidInput(self):
        '''
        check if output is false for empty input at second string
        '''
        output = MinWindowSubstring.MinWindowSubstring(["aaddef", ""])
        self.assertEqual(output, False)

    def test_NotValidInput2(self):
        '''
        checkif output is false when input is empty at first string
        '''
        output = MinWindowSubstring.MinWindowSubstring(["", "ass"])
        self.assertEqual(output, False)

    def test_NotValidInput3(self):
        '''
        check if output is false for both input strings empty
        '''
        output = MinWindowSubstring.MinWindowSubstring(["", ""])
        self.assertEqual(output, False)    
    #endregion
    
if __name__ == "__main__":
    '''
    main method of unittests class
    '''
    unittest.main()        