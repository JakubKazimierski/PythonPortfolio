'''
Unittests for CheckNums.py
October 2020 Jakub Kazimierski
'''

import unittest
import CheckNums

class test_CheckNums(unittest.TestCase):
    '''
    Class contains unittests for CheckNums.py
    '''

    #region Unittests
    def test_TrueOutput(self):
        '''
        Checks if output is equal true
        if num1 from input is less than num2 from input.
        '''
        output = CheckNums.CheckNums(1,11)
        self.assertEqual(output, "true")

    def test_EqualNumbers(self):
        '''
        Checks if output is equal -1
        if num1 from input is equal num2 from input.
        '''
        output = CheckNums.CheckNums(-2,-2)
        self.assertEqual(output, "-1")

    def test_FalseOutput(self):
        '''
        Checks if output is equal false
        if num1 from input is greater than num2 from input.
        '''
        output = CheckNums.CheckNums(32,-2)
        self.assertEqual(output, "false")
    #endregion


if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()