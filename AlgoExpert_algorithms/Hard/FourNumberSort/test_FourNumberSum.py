'''
Unittests for FourNumberSum.py
February 2021 Jakub Kazimierski
'''

import unittest
from FourNumberSum import fourNumberSum

class test_FourNumberSum(unittest.TestCase):    
    '''
    Class with unittests for FourNumberSum.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''
        self.input_arr = [7, 6, 4, -1, 1, 2]
        self.targetSum = 16

        self.output = [[7, 6, 4, -1], [7, 6, 1, 2]]

        return self.input_arr, self.targetSum, self.output

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr, targetSum, output_arr  = self.setUp()
        output = fourNumberSum(input_arr, targetSum)
        self.assertEqual(output, output_arr)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()