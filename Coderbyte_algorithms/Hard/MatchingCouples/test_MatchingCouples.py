'''
Unittests for MatchingCouples.py
January 2021 Jakub Kazimierski
'''

import unittest
import MatchingCouples

class test_MatchingCouples(unittest.TestCase):    
    '''
    Class with unittests for LCS.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = MatchingCouples.MatchingCouples([10, 5, 4])
        self.assertEqual(output, 900)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()