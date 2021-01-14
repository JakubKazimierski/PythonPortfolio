'''
Unittests for FormattedNumber.py
December 2020 Jakub Kazimierski
'''

import unittest
import FormattedNumber

class test_FormattedNumber(unittest.TestCase):    
    '''
    Class with unittests for FormattedNumber.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = FormattedNumber.FormattedNumber(["01,093,22.04"])
        self.assertEqual(output, "false")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()