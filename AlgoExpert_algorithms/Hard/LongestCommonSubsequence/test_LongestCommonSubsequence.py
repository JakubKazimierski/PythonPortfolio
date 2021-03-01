'''
Unittests for LongestCommonSubsequence.py
March 2021 Jakub Kazimierski
'''


import unittest
from LongestCommonSubsequence import longestCommonSubsequence

class test_LongestCommonSubsequence(unittest.TestCase):    
    '''
    Class with unittests for LongestCommonSubsequence.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.input_str_1 = "ZXVVYZW"
        self.input_str_2 = "XKYKZPW"

        self.output = ["X", "Y", "Z", "W"]

        return self.input_str_1, self.input_str_2, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        input_str_1, input_str_2, output = self.setUp()
        output_method = longestCommonSubsequence(input_str_1, input_str_2)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()