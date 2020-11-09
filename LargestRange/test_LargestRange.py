'''
TestUnits for LargestRange from algoexpert
October 2020 Jakub Kazimierski
'''

import unittest
import LargestRange

class test_LargestRange(unittest.TestCase):
    '''
    class with unittests for LargestRange problem
    '''
    #region Unittests
    def test_ProperOutput(self):
        '''
        test if returned output is expected range
        '''
        output = LargestRange.LargestRange([1,11,3,0,15,5,2,4,10,7,12,6])
        self.assertEqual(output, [0,7])

    def test_ProperOutput2(self):
        '''
        test if returned output is not equal false range
        '''
        output = LargestRange.LargestRange([1,11,3,0,15,5,2,4,10,7,12,6])
        self.assertNotEqual(output, [1,7])

    def test_NotValidInput(self):
        '''
        test output for not proper input
        '''
        output = LargestRange.LargestRange([])
        self.assertEqual(output, [0,0])

    def test_ProperOutputNegativeValues(self):
        '''
        test method for negative numbers
        '''
        output = LargestRange.LargestRange([-1,-11,-3,0,-15,-5,-2,-4,-10,-7,-12,-6])
        self.assertEqual(output, [-7, 0])

    def test_ProperOutputMixedValues(self):
        '''
        test method for positive and negative intigers
        '''
        output = LargestRange.LargestRange([-1,11,-3,0,15,5,-2,-4,10,7,12,6])
        self.assertEqual(output, [-4, 0])
    #endregion


if __name__ == "__main__":
    '''
    main method of unittests class
    '''
    unittest.main()