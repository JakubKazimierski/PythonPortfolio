'''
Unittests for SubarraySort.py
February 2021 Jakub Kazimierski
'''

import unittest
from SubarraySort import subarraySort

class test_SubarraySort(unittest.TestCase):    
    '''
    Class with unittests for SubarraySort.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''
        self.input_arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

        self.output = [3, 9]

        return self.input_arr, self.output

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr, output_arr  = self.setUp()
        output = subarraySort(input_arr)
        self.assertEqual(output, output_arr)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()