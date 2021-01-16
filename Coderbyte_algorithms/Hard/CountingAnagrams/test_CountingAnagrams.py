'''
Unittests for CountingAnagrams.py
January 2021 Jakub Kazimierski
'''

import unittest
import CountingAnagrams

class test_CountingAnagrams(unittest.TestCase):    
    '''
    Class with unittests for CountingAnagrams.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = "dog god dog"
        output = CountingAnagrams.CountingAnagrams(input_val)
        self.assertEqual(output, 1)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()