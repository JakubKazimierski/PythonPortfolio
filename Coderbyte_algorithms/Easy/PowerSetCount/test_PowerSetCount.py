'''
Unittests for PowerSetCount.py
December 2020 Jakub Kazimierski
'''

import unittest
import PowerSetCount

class test_PowerSetCount(unittest.TestCase):
    '''
    Class contains unittests for
    PowerSetCount.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks is output is as expected.
        '''
        output = PowerSetCount.PowerSetCount([1, 2, 3])
        self.assertEqual(output, 8)

    def test_WrongInput(self):
        '''
        Checks is output is equal -1 if input is wrong.
        '''
        output = PowerSetCount.PowerSetCount(10111)
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()