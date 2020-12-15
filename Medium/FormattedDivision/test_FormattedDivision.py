'''
Unittests for FormattedDivision.py
December 2020 Jakub Kazimierski
'''

import unittest
import FormattedDivision

class test_FormattedDivision(unittest.TestCase):    
    '''
    Class with unittests for FormattedDivision.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = FormattedDivision.FormattedDivision(123456789, 10000)
        self.assertEqual("12,345.6789", output)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()