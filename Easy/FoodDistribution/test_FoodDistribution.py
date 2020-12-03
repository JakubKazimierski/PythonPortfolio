'''
Unittests for FoodDistribution.py
December 2020 Jakub Kazimierski
'''

import unittest
import FoodDistribution

class test_FoodDistribution(unittest.TestCase):
    '''
    Class contains unittests for
    FoodDistribution.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = FoodDistribution.FoodDistribution([5, 2, 3, 4, 5])
        self.assertEqual(output, 1)

    def test_NextExample(self):
        '''
        Checks if output is as expected.
        '''
        output = FoodDistribution.FoodDistribution([3, 2, 1, 0, 4, 1, 0])
        self.assertEqual(output, 4)

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()