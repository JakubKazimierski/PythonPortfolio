'''
Unittests for DivisionStringified.py
November 2020 Jakub Kazimierski
'''

import unittest
import DivisionStringifiedSimplier

class test_DivisionStringified(unittest.TestCase):
    '''
    Class contains unittests for DivisionStringified.py
    '''

    #region Unittests
    def test_WrongTypeInput(self):
        '''
        Checks if input has correct type.
        '''
        output = DivisionStringifiedSimplier.DivisionStringified("1",2)
        self.assertEqual(output, "Not correct input")

    def test_ComaTests(self):
        '''
        Checks if comas in digit are at correct places.
        '''
        output = DivisionStringifiedSimplier.DivisionStringified(1000000,1)
        self.assertEqual(output, "1,000,000")

    def test_RoundingTests(self):
        '''
        Checks if function round division output correctly. 
        '''
        output = DivisionStringifiedSimplier.DivisionStringified(9,2)
        self.assertEqual(output, "5")

    def test_BigNumsDivision(self):
        '''
        Checks if for big nums function work properly.
        '''
        output = DivisionStringifiedSimplier.DivisionStringified(123456789 , 10000)
        self.assertEqual(output, "12,346")

    def test_DivisionByZero(self):
        '''
        Checks if for num2 equal 0 assertion works properly.
        '''
        output = DivisionStringifiedSimplier.DivisionStringified(123456789 , 0)
        self.assertEqual(output, "Not correct input")

    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests' class.
    '''
    unittest.main()