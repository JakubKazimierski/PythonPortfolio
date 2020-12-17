'''
Unittests for StringReduction.py
December 2020 Jakub Kazimierski
'''

import unittest
import StringReduction

class test_StringReduction(unittest.TestCase):    
    '''
    Class with unittests for StringReduction.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = StringReduction.StringReduction( "bcab")
        self.assertEqual(output, 1)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()