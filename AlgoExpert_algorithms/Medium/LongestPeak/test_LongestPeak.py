'''
Unittests for LongestPeak.py
January 2021 Jakub Kazimierski
'''

import unittest
import LongestPeak

class test_LongestPeak(unittest.TestCase):    
    '''
    Class with unittests for LongestPeak.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr  = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        output = LongestPeak.longestPeak(input_arr)
        self.assertEqual(output, 6)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()