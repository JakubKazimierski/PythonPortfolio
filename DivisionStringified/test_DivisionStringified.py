'''
Unittests for DivisionStringified.py
November 2020 Jakub Kazimierski
'''

import unittest
import DivisionStringified

class test_DivisionStringified(unittest.TestCase):
    '''
    Class contains unittests for DivisionStringified.py
    '''

    #region Unittests
    def test_WrongTypeInput(self):
        '''
        Checks if input has correct type.
        '''
        output = DivisionStringified.DivisionStringified(1.0,2)
        self.assertEqual(output, "Input type has to be Integer")

    def test_ComaTests(self):
        '''
        Checks if comas in digit are at correct places.
        '''
        output = DivisionStringified.DivisionStringified(1000000,1)
        self.assertEqual(output, "1,000,000")

    def test_RoundingTests(self):
        '''
        Checks if function round division output correctly. 
        '''
        output = DivisionStringified.DivisionStringified(9,2)
        self.assertEqual(output, "5")

    def test_BigNumsDivision(self):
        '''
        Checks if for big nums function work properly.
        '''
        output = DivisionStringified.DivisionStringified(123456789 , 10000)
        self.assertEqual(output, "12,346")

    def test_DivisionByZero(self):
        '''
        Checks if for num2 equal 0 assertion works properly.
        '''
        output = DivisionStringified.DivisionStringified(123456789 , 0)
        self.assertEqual(output, "num2 cannot be 0")

    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests' class.
    '''
    unittest.main()