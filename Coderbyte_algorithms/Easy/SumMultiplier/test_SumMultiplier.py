'''
Unittests for SumMultiplier.py
December 2020 Jakub Kazimierski
'''

import unittest
import SumMultiplier

class test_SumMultiplier(unittest.TestCase):    
    '''
    Class with unittests for SumMultiplier.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = SumMultiplier.SumMultiplier([2, 5, 6, -6, 16, 2, 3, 6, 5, 3])
        self.assertEqual(output, "true")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = SumMultiplier.SumMultiplier(["a", "b"])
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()