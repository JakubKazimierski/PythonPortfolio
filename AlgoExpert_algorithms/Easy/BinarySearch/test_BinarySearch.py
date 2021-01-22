'''
Unittests for BinarySearch.py
January 2021 Jakub Kazimierski
'''

import unittest
import BinarySearch

class test_BinarySearch(unittest.TestCase):    
    '''
    Class with unittests for BinarySearch.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr   = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 33
        output = BinarySearch.binarySearch(input_arr, target)
        self.assertEqual(output, 3)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()