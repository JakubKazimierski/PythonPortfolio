'''
Unittests for BracketCombinations.py
January 2021 Jakub Kazimierski
'''

import unittest
import BracketCombinations

class test_BracketCombinations(unittest.TestCase):    
    '''
    Class with unittests for BracketCombinations.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = BracketCombinations.BracketCombinations(3)
        self.assertEqual(output, 5)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()