'''
Unittests for GroupAnagrams.py
February 2021 Jakub Kazimierski
'''

import unittest
from GroupAnagrams import groupAnagrams, compare_lists

class test_GroupAnagrams(unittest.TestCase):    
    '''
    Class with unittests for GroupAnagrams.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''
        self.input = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
        self.output = [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
        return self.input, self.output

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr, output_arr  = self.setUp()
        output = groupAnagrams(input_arr)
        
        self.assertEqual(compare_lists(output, output_arr), True)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()