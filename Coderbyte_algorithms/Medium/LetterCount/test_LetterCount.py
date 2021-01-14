'''
Unittests for LetterCount.py
December 2020 Jakub Kazimierski
'''

import unittest
import LetterCount

class test_LetterCount(unittest.TestCase):    
    '''
    Class with unittests for LetterCount.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = LetterCount.LetterCount("Today, is the greatest day ever!")
        self.assertEqual(output, "greatest")

    def test_NonRepeatiing(self):
        '''
        Checks if returned output is as expected.
        '''
        output = LetterCount.LetterCount("Today")
        self.assertEqual(output, "-1")


    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()