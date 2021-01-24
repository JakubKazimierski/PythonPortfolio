'''
Unittests for MonotonicArray.py
January 2021 Jakub Kazimierski
'''

import unittest
import MonotonicArray

class test_MonotonicArray(unittest.TestCase):    
    '''
    Class with unittests for MonotonicArray.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr  = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        output = MonotonicArray.monotonicArray(input_arr)
        self.assertEqual(output, True)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()