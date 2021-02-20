'''
Unittests for LargestRange.py
February 2021 Jakub Kazimierski
'''

import unittest
from LargestRange import largestRange

class test_LargestRange(unittest.TestCase):    
    '''
    Class with unittests for LargestRange.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''
        self.input_arr = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

        self.output = [0, 7]

        return self.input_arr, self.output

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr, output_arr  = self.setUp()
        output = largestRange(input_arr)
        self.assertEqual(output, output_arr)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()