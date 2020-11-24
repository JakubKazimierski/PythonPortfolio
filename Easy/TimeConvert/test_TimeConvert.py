'''
Unittests for TimeCOnvert.py
from codersbyte
October 2020 Jakub Kazimierski
'''

import unittest
import TimeConvert


class test_TimeConvert(unittest.TestCase):

    '''
    class with unittests for TimeConvert.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        check if output is as expected
        return true if is
        '''
        output = TimeConvert.TimeConvert(100)
        self.assertEqual(output, "1:40")

    def test_WrongOutput(self):
        '''
        check if after division of hours
        output has no floating numbers
        '''
        output = TimeConvert.TimeConvert(100)
        self.assertNotEqual(output, "1,6666666:40")

    def test_WrongInput(self):
        '''
        check if output is 0:0
        if input is wrong in range
        '''
        output = TimeConvert.TimeConvert(-100)
        self.assertEqual(output, "0:0")

    def test_WrongOutputFLoat(self):
        '''
        check if output is 0:0 if
        input has wrong type
        '''
        output = TimeConvert.TimeConvert(100.0)
        self.assertEqual(output, "0:0")
    #endregion


if __name__ == "__main__":
    '''
    main method of unittests class
    '''
    unittest.main()        