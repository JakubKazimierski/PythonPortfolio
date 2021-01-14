'''
Unittests for StringScramble.py
December 2020 Jakub Kazimierski
'''

import unittest
import StringScramble

class test_StringScramble(unittest.TestCase):    
    '''
    Class with unittests for StringScramble.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = StringScramble.StringScramble("rkqodlw", "world")
        self.assertEqual(output, "true")

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()