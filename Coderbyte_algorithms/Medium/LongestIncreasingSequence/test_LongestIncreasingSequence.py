'''
Unittests for LongestIncreasingSequence.py
December 2020 Jakub Kazimierski
'''

import unittest
import LongestIncreasingSequence

class test_LRU_Cache(unittest.TestCase):    
    '''
    Class with unittests for LongestIncreasingSequence.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = [4, 3, 5, 1, 6]
        output = LongestIncreasingSequence.LongestIncreasingSequence(input_val)
        self.assertEqual(output, 3)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()