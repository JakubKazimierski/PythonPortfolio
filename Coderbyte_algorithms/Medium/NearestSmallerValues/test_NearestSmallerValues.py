'''
Unittests for NearestSmallerValues.py
December 2020 Jakub Kazimierski
'''

import unittest
import NearestSmallerValues

class test_NearestSmallerValues(unittest.TestCase):    
    '''
    Class with unittests for NearestSmallerValues.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = [5, 2, 8, 3, 9, 12]
        output = NearestSmallerValues.NearestSmallerValues(input_val)
        self.assertEqual(output, "-1 -1 2 2 3 9")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()