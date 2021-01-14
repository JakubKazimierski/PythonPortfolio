'''
PowersOfTwo unittests class
November 2020 Jakub Kazimierski
'''

import unittest
import PowersOfTwo

class test_PowersOfTwo(unittest.TestCase):
    '''
    Class contains unittests for PowersOfTwo.py 
    '''

    #region Unittests

    def test_InputIsPowerOfTwo(self):
        '''
        Checks if output is equall true for powerOfTwo input.
        '''
        output = PowersOfTwo.PowersOfTwo(1024)
        self.assertEqual(output, "true")

    def test_NotPowerOfTwo(self):
        '''
        Checks if output is equall false if input is not power of two.
        '''
        output = PowersOfTwo.PowersOfTwo(7)
        self.assertEqual(output, "false")

    def test_NegativePowerOfTwo(self):
        '''
        Checks if output is equall to true if input is negative power of two.
        '''
        output = PowersOfTwo.PowersOfTwo(-8)
        self.assertEqual(output, "true")


    def test_NotProperInput(self):
        '''
        Checks if output is equall -1 if input type is wrong.
        '''
        output = PowersOfTwo.PowersOfTwo("7")
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittests.
    '''
    unittest.main()
