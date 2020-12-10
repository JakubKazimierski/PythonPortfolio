'''
Unittests for StringPeriods.py
December 2020 Jakub Kazimierski
'''

import unittest
import StringPeriods

class test_StringPeriods(unittest.TestCase):
    '''
    Class contains unittests for StringPeriods.py
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = StringPeriods.StringPeriods("abcababcababcab")
        self.assertEqual(output, "abcab")

    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = StringPeriods.StringPeriods(12)
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittests.
    '''
    unittest.main()
