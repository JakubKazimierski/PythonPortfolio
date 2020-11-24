'''
Unittests for FirstFactorial.py
October 2020 Jakub Kazimierski
'''

import unittest
import FirstFactorialRecurency


class test_FirstFactorial(unittest.TestCase):
    '''
    Class contains unittests for FirstFactorial.py
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        Checks if counted factorial in output is correct.
        '''
        output = FirstFactorialRecurency.FirstFactorial(4)
        self.assertEqual(output, 24)

    #range for input is [1, 18]
    def test_ProperOutputNegatives(self):
        '''
        Checks if output is equal -1 for numbers out of range.
        '''
        output = FirstFactorialRecurency.FirstFactorial((-4))
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittests.
    '''
    unittest.main()
