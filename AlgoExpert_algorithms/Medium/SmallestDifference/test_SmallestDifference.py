'''
Unittests for SmallestDifference.py
January 2021 Jakub Kazimierski
'''

import unittest
import SmallestDifference

class test_SmallestDifference(unittest.TestCase):    
    '''
    Class with unittests for SmallestDifference.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr_I = [-1, 5, 10, 20, 28, 3]
        input_arr_II = [26, 134, 135, 15, 17]
        output = SmallestDifference.smallestDifference(input_arr_I, input_arr_II)
        self.assertEqual(output, [28, 26])
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()