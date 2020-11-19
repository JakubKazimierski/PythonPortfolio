'''
Unitests for LargestRange from algoexpert
October 2020 Jakub Kazimierski
'''

import unittest
import LargestRange

class test_LargestRange(unittest.TestCase):
    '''
    Class contains unittests for LargestRange.py
    '''
    #region Unittests
    def test_ProperOutput(self):
        '''
        Checks if returned output values are expected range.
        '''
        output = LargestRange.LargestRange([1,11,3,0,15,5,2,4,10,7,12,6])
        self.assertEqual(output, [0,7])

    def test_NotValidInput(self):
        '''
        Checks if assertion works for not proper input type.
        '''
        output = LargestRange.LargestRange(["1","2"])
        self.assertEqual(output, "Wrong input")

    def test_ProperOutputNegativeValues(self):
        '''
        Checks method for negative values of numbers.
        '''
        output = LargestRange.LargestRange([-1,-11,-3,0,-15,-5,-2,-4,-10,-7,-12,-6])
        self.assertEqual(output, [-7, 0])

    def test_ProperOutputMixedValues(self):
        '''
        Checks method for positive and negative values of numbers mixed.
        '''
        output = LargestRange.LargestRange([-1,11,-3,0,15,5,-2,-4,10,7,12,6])
        self.assertEqual(output, [-4, 0])
    #endregion


if __name__ == "__main__":
    '''
    Main method of unittests class.
    '''
    unittest.main()