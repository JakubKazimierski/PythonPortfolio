'''
Unittests for LongestPalindromicSubstring.py
February 2021 Jakub Kazimierski
'''

import unittest
from LongestPalindromicSubstring import longestPalindromicSubstring

class test_LongestPalindromicSubstring(unittest.TestCase):    
    '''
    Class with unittests for LongestPalindromicSubstring.py
    '''

    def setUp(self):
        '''
        SetUp string for tests.
        '''

        self.input_string = "abaxyzzyxf"
        self.output_string = "xyzzyx"

        return self.input_string, self.output_string

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_str, output_str = self.setUp()

        output = longestPalindromicSubstring(input_str)

        self.assertEqual(output, output_str)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()