'''
Unittests for SecondGreatLow.py
November 2020 Jakub Kazimierski
'''

import unittest
import SecondGreatLow

class test_SecondGreatLow(unittest.TestCase):
    '''
    Class contains unittests for SecondGreatLow.py
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = SecondGreatLow.SecondGreatLow([1, 42, 42, 180])
        self.assertEqual(output, "42 42")

    def test_TwoValuesArr(self):
        '''
        Checks if algorithm works properly if array is lenght of 2.
        '''
        output = SecondGreatLow.SecondGreatLow([1, 180])
        self.assertEqual(output, "180 1")

    def test_NegativeValuesArr(self):
        '''
        Checks if algorithm works properly with negative numbers.
        '''
        output = SecondGreatLow.SecondGreatLow([1, -43, -2, 180])
        self.assertEqual(output, "-2 1")

    def test_WrongInput(self):
        '''
        Cheks if output is equal -1 for wrong input type.
        '''
        output = SecondGreatLow.SecondGreatLow(["1", "-43", -2, 180])
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittests.
    '''
    unittest.main()