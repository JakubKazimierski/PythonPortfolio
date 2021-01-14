'''
Unittestst for LongestConsecutive.py
December 2020 Jakub Kazimierski
'''

import unittest
import LongestConsecutive

class test_LongestConsecutive(unittest.TestCase):    
    '''
    Class with unittests for LongestConsecutive.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = LongestConsecutive.LongestConsecutive([4, 3, 8, 1, 2, 6, 100, 9])
        self.assertEqual(output, 4)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()