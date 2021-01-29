'''
Unittests for NumbersOfWaysToMakeChange.py
January 2021 Jakub Kazimierski
'''

import unittest
from NumbersOfWaysToMakeChange import numberOfWaysToMakeChange

class test_NumbersOfWaysToMakeChange(unittest.TestCase):    
    '''
    Class with unittests for NumbersOfWaysToMakeChange.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr = [1, 5]
        input_val = 6
        output = numberOfWaysToMakeChange(input_val, input_arr)
        self.assertEqual(output, 2)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()