'''
Unittests for ThreeNumberSum.py
January 2021 Jakub Kazimierski
'''

import unittest
import ThreeNumberSum

class test_ThreeNumberSum(unittest.TestCase):    
    '''
    Class with unittests for ThreeNumberSum.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr  = [12, 3, 1, 2, -6, 5, -8, 6]
        target = 0
        output = ThreeNumberSum.threeNumberSum(input_arr, target)
        self.assertEqual(output, [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()