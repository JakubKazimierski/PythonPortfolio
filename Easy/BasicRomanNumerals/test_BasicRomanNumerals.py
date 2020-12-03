'''
Unittests for BasicRomanNumerals.py
December 2020 Jakub Kazimierski
'''

import unittest
import BasicRomanNumerals

class test_BasicRomanNumerals(unittest.TestCase):
    '''
    Class contains unittests for
    BasicRomanNumerals.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = BasicRomanNumerals.BasicRomanNumerals("XLVI")
        self.assertEqual(output, 46)

    def test_WrongInput(self):
        '''
        Checks if output is equal -1 if input is wrong.
        '''
        output = BasicRomanNumerals.BasicRomanNumerals(111)
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()