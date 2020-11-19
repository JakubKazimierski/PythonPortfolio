'''
Unittests for FirstReverse.py from Coderbyte
October 2020 Jakub Kazimierski
'''

import unittest
import FirstReverse

class test_FirstReverse(unittest.TestCase):
    '''
    Class contains unittests for FirstReverse.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is in reverse order
        as expected.
        '''
        output = FirstReverse.FirstReverse("abcd")
        self.assertEqual(output, "dcba")

    def test_EmptyOutput(self):
        '''
        Checks if output is empty for empty input.
        '''
        output = FirstReverse.FirstReverse("")
        self.assertEqual(output, "")

    def test_VariousCharctersStringOutput(self):
        '''
        Checks if string containing other signs 
        than letters is reversed as expected.
        '''
        output = FirstReverse.FirstReverse("12345?")
        self.assertEqual(output, "?54321")

    def test_WrongInputType(self):
        '''
        Checks if output is equal -1 for wrong input type.
        '''
        output = FirstReverse.FirstReverse(32)
        self.assertEqual(output, -1)


    #endregion
    
if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()        