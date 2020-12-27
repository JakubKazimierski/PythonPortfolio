'''
Unittestst for TernaryConverter.py
December 2020 Jakub Kazimierski
'''

import unittest
import TernaryConverter

class test_TernaryConverter(unittest.TestCase):    
    '''
    Class with unittests for TernaryConverter.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = TernaryConverter.TernaryConverter(12)
        self.assertEqual(output, 110)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()