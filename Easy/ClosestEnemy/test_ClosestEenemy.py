'''
Unittests for ClosestEnemy.py
December 2020 Jakub Kazimierski
'''

import unittest
import ClosestEnemy

class test_ClosestEnemy(unittest.TestCase):
    '''
    Class contains unittests for ClosestEnemy.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is sorted in alphabetical order.
        '''
        output = ClosestEnemy.ClosestEnemy([1, 0, 0, 0, 2, 2, 2])
        self.assertEqual(output, 4)

    def test_WrongInput(self):
        '''
        Checks if output is -1 when input is wrong type.
        '''
        output = ClosestEnemy.ClosestEnemy(12)
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests' Class.
    '''
    unittest.main()