'''
Unittests for MaxSumIncreasingSubsequence.py
February 2021 Jakub Kazimierski
'''

import unittest
from MaxSumIncreasingSubsequence import maxSumIncreasingSubsequence

class test_MaxSumIncreasingSubsequence(unittest.TestCase):    
    '''
    Class with unittests for MaxSumIncreasingSubsequence.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.input_arr = [10, 70, 20, 30, 50, 11, 30]
        self.output = [110, [10, 20, 30, 50]]

        return self.input_arr, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        input_arr, output = self.setUp()
        output_method = maxSumIncreasingSubsequence(input_arr)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()