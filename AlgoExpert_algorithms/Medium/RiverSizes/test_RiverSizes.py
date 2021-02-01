'''
Unittests for RiverSizes.py
January 2021 Jakub Kazimierski
'''

import unittest
import RiverSizes

class test_RiverSizes(unittest.TestCase):    
    '''
    Class with unittests for RiverSizes.py
    '''

    def setUp(self):
        '''
        SetUp matrix for tests.
        '''
        self.matrix = [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0],
        ]

        return self.matrix

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''

        input_matrix = self.setUp()
        output_arr = [1, 2, 2, 2, 5]
        output = RiverSizes.riverSizes(input_matrix)
        self.assertEqual(output.sort(), output_arr.sort())
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()