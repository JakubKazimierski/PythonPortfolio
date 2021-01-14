'''
Unittests for TimeConvert.py
October 2020 Jakub Kazimierski
'''

import unittest
import TimeConvert


class test_TimeConvert(unittest.TestCase):
    '''
    Class contains unittests for TimeConvert.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = TimeConvert.TimeConvert(100)
        self.assertEqual(output, "1:40")

    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for negative input.
        '''
        output = TimeConvert.TimeConvert(-100)
        self.assertEqual(output, -1)

    def test_InputFloat(self):
        '''
        Checks if output is proper if input is float.
        '''
        output = TimeConvert.TimeConvert(100.0)
        self.assertEqual(output, "1:40")
    #endregion


if __name__ == "__main__":
    '''
    Main method of unittests.
    '''
    unittest.main()        