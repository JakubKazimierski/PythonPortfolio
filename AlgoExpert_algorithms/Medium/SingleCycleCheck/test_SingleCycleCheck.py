'''
Unittests for SingleCycleCheck.py
January 2021 Jakub Kazimierski
'''

import unittest
from SingleCycleCheck import hasSingleCycle

class test_SingleCycleCheck(unittest.TestCase):    
    '''
    Class with unittests for SingleCycleCheck.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr = [2, 3, 1, -4, -4, 2]
        output = hasSingleCycle(input_arr)
        self.assertEqual(output, True)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()