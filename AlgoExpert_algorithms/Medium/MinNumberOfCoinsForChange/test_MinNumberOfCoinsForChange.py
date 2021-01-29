'''
Unittests for MinNumberOfCoinsForChange.py
January 2021 Jakub Kazimierski
'''

import unittest
from MinNumberOfCoinsForChange import minNumberOfCoinsForChange

class test_MinNumberOfCoinsForChange(unittest.TestCase):    
    '''
    Class with unittests for MinNumberOfCoinsForChange.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr = [1, 5, 10]
        input_val = 7
        output = minNumberOfCoinsForChange(input_val, input_arr)
        self.assertEqual(output, 3)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()