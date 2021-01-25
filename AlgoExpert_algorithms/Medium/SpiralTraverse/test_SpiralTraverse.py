'''
Unittests for SpiralTraverse.py
January 2021 Jakub Kazimierski
'''

import unittest
import SpiralTraverse

class test_SpiralTraverse(unittest.TestCase):    
    '''
    Class with unittests for SpiralTraverse.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr  = [
        [1,   2,  3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10,  9,  8, 7],
        ]
        output_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        output = SpiralTraverse.spiralTraverse(input_arr)
        self.assertEqual(output, output_arr)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()