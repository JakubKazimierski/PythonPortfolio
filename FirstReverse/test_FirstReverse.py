'''
Unittests for FirstReverse from codersbyte
October 2020 Jakub Kazimierski
'''

import unittest
import FirstReverse

class test_FirstReverse(unittest.TestCase):
    '''
    class with unittests for FirstReverse from codersbyte
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        test checks if output is in reverse oder
        as expected
        '''
        output = FirstReverse.FirstReverse("abcd")
        self.assertEqual(output, "dcba")

    def test_EmptyOutput(self):
        '''
        test if output is empty for empty input
        '''
        output = FirstReverse.FirstReverse("")
        self.assertEqual(output, "")

    def test_VariousCharctersStringOutput(self):
        '''
        test if other characters than letters
        are revrsed as expected
        '''
        output = FirstReverse.FirstReverse("12345?")
        self.assertEqual(output, "?54321")
    #endregion
    
if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()        