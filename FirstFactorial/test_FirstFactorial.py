'''
Unittests for first fatorial
October 2020 Jakub Kazimierski
'''

import unittest
import FirstFactorial


class test_FirstFactorial(unittest.TestCase):
    '''
    class of unittests for first factorial
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        method check for expected output
        '''
        output = FirstFactorial.FirstFactorial(4)
        self.assertEqual(output, 24)

    #range for input is [0, 18]
    def test_ProperOutputNegatives(self):
        '''
        method check output for numbers out of range
        '''
        output = FirstFactorial.FirstFactorial((-4))
        self.assertEqual(output, -1)

    def test_ProperOutputZero(self):
        '''
        method check if output is correct for 0
        '''
        output = FirstFactorial.FirstFactorial(0)
        self.assertEqual(output, 1)
    #endregion

if __name__ == "__main__":
    '''
    main method of unittests
    '''
    unittest.main()
