'''
Unittests for TwoSum.py
December 2020 Jakub Kazimierski
'''

import unittest
import TwoSum

class test_TwoSum(unittest.TestCase):
    '''
    Class contains unittests for TwoSum.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = TwoSum.TwoSum([7, 3, 5, 2, -4, 8, 11])
        self.assertEqual(output, "5,2 -4,11")

    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = TwoSum.TwoSum(11)
        self.assertEqual(output, -1)

    #endregion


if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()