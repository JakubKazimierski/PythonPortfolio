'''
Unittests for MinRewards.py
February 2021 Jakub Kazimierski
'''

import unittest
from MinRewards import minRewards

class test_MinRewards(unittest.TestCase):    
    '''
    Class with unittests for MinRewards.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''
        self.input_arr = [8, 4, 2, 1, 3, 6, 7, 9, 5]

        self.output = 25

        return self.input_arr, self.output

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr, output_arr  = self.setUp()
        output = minRewards(input_arr)
        self.assertEqual(output, output_arr)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()