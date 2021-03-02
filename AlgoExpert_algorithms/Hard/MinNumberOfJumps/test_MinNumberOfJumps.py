'''
Unittests for MinNumberOfJumps.py
March 2021 Jakub Kazimierski
'''

import unittest
from MinNumberOfJumps import minNumberOfJumps

class test_MinNumberOfJumps(unittest.TestCase):    
    '''
    Class with unittests for MinNumberOfJumps.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.input_arr = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
        self.output = 4

        return self.input_arr, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        input_arr, output = self.setUp()
        output_method = minNumberOfJumps(input_arr)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()