'''
PowersOfTwo unittests class
November 2020 Jakub Kazimierski
'''

import unittest
import PowersOfTwo

class test_PowersOfTwo(unittest.TestCase):
    '''
    class contains unittests for
    PowersOfTwo.py 
    '''

    #region Unittests

    def test_InputIsPowerOfTwo(self):
        '''
        check if output is equall
        to true for powerOfTwo input
        '''
        output = PowersOfTwo.PowersOfTwo(1024)
        self.assertEqual(output, "true")

    def test_NotPowerOfTwo(self):
        '''
        check if output is equall
        to false if itput is not power of two
        '''
        output = PowersOfTwo.PowersOfTwo(7)
        self.assertEqual(output, "false")

    def test_NegativePowerOfTwo(self):
        '''
        check if output is equall
        to true if itput is negative power of two
        '''
        output = PowersOfTwo.PowersOfTwo(-8)
        self.assertEqual(output, "true")


    def test_NotProperInput(self):
        '''
        check if output is equall
        to -1 if input type is wrong
        '''
        output = PowersOfTwo.PowersOfTwo("7")
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    main method of unittests
    '''
    unittest.main()
