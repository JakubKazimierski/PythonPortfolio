'''
Unittestst for StepWalking.py
January 2021 Jakub Kazimierski
'''

import unittest
import StepWalking

class test_StepWalking(unittest.TestCase):    
    '''
    Class with unittests for StepWalking.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = StepWalking.StepWalking(1)
        self.assertEqual(output, 3)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()