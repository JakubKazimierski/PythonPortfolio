'''
Unittests for TwoNumberSum.py
January 2021 Jakub Kazimierski
'''

import unittest
import TwoNumberSum

class test_TwoNumberSum(unittest.TestCase):    
    '''
    Class with unittests for TwoNumberSum.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr = [3, 5, -4, 8, 11, 1, -1, 6]
        target_sum = 10
        output = TwoNumberSum.twoNumberSum(input_arr, target_sum)
        self.assertEqual(set(output), set([11, -1]))
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()