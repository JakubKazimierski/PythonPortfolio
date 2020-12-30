'''
Unittests for StringExpression.py
December 2020 Jakub Kazimierski
'''

import unittest
import StringExpression

class test_StringExpression(unittest.TestCase):    
    '''
    Class with unittests for StringExpression.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = StringExpression.StringExpression("foursixminustwotwoplusonezero")
        self.assertEqual(output, "threefour")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()