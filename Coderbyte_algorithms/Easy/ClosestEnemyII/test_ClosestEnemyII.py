'''
Unittests for ClosestEnemyII.py
December 2020 Jakub Kazimierski
'''

import unittest
import ClosestEnemyII

class test_ClosestEnemyII(unittest.TestCase):
    '''
    Class contains unittests for ClosestEnemyII.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is sorted in alphabetical order.
        '''
        output = ClosestEnemyII.ClosestEnemyII(["0000", "2010", "0000", "2002"])
        self.assertEqual(output, 2)

    def test_ZeroOutput(self):
        '''
        Checks if output is equal 0 if matrix has no 2.
        '''
        output = ClosestEnemyII.ClosestEnemyII(["0000", "1000", "0000", "0000"])
        self.assertEqual(output, 0)

    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests' Class.
    '''
    unittest.main()