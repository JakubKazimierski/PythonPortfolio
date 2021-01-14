'''
Unittests for LRU_Cache.py
December 2020 Jakub Kazimierski
'''

import unittest
import LRU_Cache

class test_LRU_Cache(unittest.TestCase):    
    '''
    Class with unittests for LRU_Cache.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["A", "B", "C", "D", "A", "E", "D", "Z"]
        output = LRU_Cache.LRU_Cache(input_val)
        self.assertEqual(output, "C-A-E-D-Z")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()