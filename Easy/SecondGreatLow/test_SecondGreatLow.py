'''
Unittests for SecondGreatLow.py
November 2020 Jakub Kazimierski
'''

import unittest
import SecondGreatLow

class test_SecondGreatLow(unittest.TestCase):
    '''
    class contains unittests
    for SecondGreatLow.py
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        check if output is as expected
        '''
        output = SecondGreatLow.SecondGreatLow([1, 42, 42, 180])
        self.assertEqual(output, "42 42")

    def test_TwoValuesArr(self):
        '''
        check if algorithm works
        properly if array is length 2
        '''
        output = SecondGreatLow.SecondGreatLow([1, 180])
        self.assertEqual(output, "1 180")

    def test_NegativeValuesArr(self):
        '''
        check if algorithm works
        properly with negative numbers
        '''
        output = SecondGreatLow.SecondGreatLow([1, -43, -2, 180])
        self.assertEqual(output, "-2 1")


    def test_WrongInput(self):
        '''
        check if for wrong input
        output is -1
        '''
        output = SecondGreatLow.SecondGreatLow([1])
        self.assertEqual(output, -1)
    #endregion

if __name__ == "__main__":
    '''
    main method of unittests
    class
    '''
    unittest.main()