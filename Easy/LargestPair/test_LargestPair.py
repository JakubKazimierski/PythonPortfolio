'''
Unittests for LargestPair.py
December 2020 Jakub Kazimierski
'''

import unittest
import LargestPair

class test_LargestPair(unittest.TestCase):
    '''
    Class contains unittests for CheckNums.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = LargestPair.LargestPair(4759472)
        self.assertEqual(output, 94)

    #endregion


if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()