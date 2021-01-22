'''
Unittests for FindThreeLargestNumbers.py
January 2021 Jakub Kazimierski
'''

import unittest
import FindThreeLargestNumbers

class test_FindThreeLargestNumbers(unittest.TestCase):    
    '''
    Class with unittests for FindThreeLargestNumbers.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr = [10, 5, 9, 10, 12]
        output = FindThreeLargestNumbers.findThreeLargestNumbers(input_arr)
        self.assertEqual(output, [10, 10, 12])
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()