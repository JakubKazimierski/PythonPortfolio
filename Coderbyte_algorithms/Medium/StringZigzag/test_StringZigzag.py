'''
Unittestst for StringZigzag.py
December 2020 Jakub Kazimierski
'''

import unittest
import StringZigzag

class test_StringZigzag(unittest.TestCase):    
    '''
    Class with unittests for StringZigzag.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = StringZigzag.StringZigzag(["coderbyte", "3"])
        self.assertEqual(output, "creoebtdy")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()