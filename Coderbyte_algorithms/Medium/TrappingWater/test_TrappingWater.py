'''
Unittests for TrappingWater.py
December 2020 Jakub Kazimierski
'''

import unittest
import TrappingWater

class test_TrappingWater(unittest.TestCase):    
    '''
    Class with unittests for TrappingWater.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = TrappingWater.TrappingWater([3, 0, 0, 2, 0, 4])
        self.assertEqual(output, 10)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()