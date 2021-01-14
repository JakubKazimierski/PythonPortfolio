'''
Unittests for SerialNumber.py
December 2020 Jakub Kazimierski
'''

import unittest
import SerialNumber

class test_SerialNumber(unittest.TestCase):
    '''
    Class contains unittests for SerialNumber.py
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = SerialNumber.SerialNumber("224.315.218")
        self.assertEqual(output, "true")

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittests.
    '''
    unittest.main()
