'''
Unittests for Kadane_s_Algorithm.py
January 2021 Jakub Kazimierski
'''

import unittest
from Kadane_s_Algorithm import kadanesAlgorithm

class test_Kadane_s_Algorithm(unittest.TestCase):    
    '''
    Class with unittests for Kadane_s_Algorithm.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
        output = kadanesAlgorithm(input_arr)
        self.assertEqual(output, 19)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()