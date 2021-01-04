'''
Unittests for PatternChaser.py
January 2021 Jakub Kazimierski
'''

import unittest
import PatternChaser

class test_PatternChaser(unittest.TestCase):    
    '''
    Class with unittests for PatternChaser.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        pass
        output = PatternChaser.PatternChaser("aabejiabkfabed")
        self.assertEqual(output, "yes abe")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()