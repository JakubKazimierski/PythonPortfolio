'''
Unittests for SortedSquaredArray.py
March 2021 Jakub Kazimierski
'''

import unittest
from SortedSquaredArray import sortedSquaredArray

class test_SortedSquaredArray(unittest.TestCase):    
    '''
    Class with unittests for SortedSquaredArray.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.input_arr = [1, 2, 3, 5, 6, 8, 9]

        self.output = [1, 4, 9, 25, 36, 64, 81]

        return self.input_arr, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        arr, output = self.setUp()
        output_method = sortedSquaredArray(arr)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()