'''
Unittests for DivisionStringified.py
November 2020 Jakub Kazimierski
'''

import unittest
import DivisionStringified

class test_DivisionStringified(unittest.TestCase):
    '''
    class contains unittests for DivisionStringified.py
    '''

    #region Unittests
    def test_WrongTypeInput(self):
        '''
        checks if input is as expected
        '''
        output = DivisionStringified.DivisionStringified(1.0,2)
        self.assertEqual(output, "Input type has to be Intiger")

    def test_ComaTests(self):
        '''
        checks if comas in digit are at correct places
        '''
        output = DivisionStringified.DivisionStringified(1000000,1)
        self.assertEqual(output, "1,000,000")

    def test_RoundingTests(self):
        '''
        checks if function round correctly output
        not for closest even num, but properly 
        '''
        output = DivisionStringified.DivisionStringified(9,2)
        self.assertEqual(output, "5")

    def test_BigNumsDivision(self):
        '''
        checks if for big nums function work properly
        '''
        output = DivisionStringified.DivisionStringified(123456789 , 10000)
        self.assertEqual(output, "12,346")


    #endregion

if __name__ == "__main__":
    '''
    main method for unittests' class
    '''
    unittest.main()