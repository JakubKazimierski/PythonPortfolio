'''
Unittests for DifferentCases.py
December 2020 Jakub Kazimierski
'''

import unittest
import DifferentCases

class test_DifferentCases(unittest.TestCase):    
    '''
    Class with unittests for DifferentCases.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = DifferentCases.DifferentCases("Daniel LikeS-coding")
        self.assertEqual(output, "DanielLikesCoding")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = DifferentCases.DifferentCases(12)
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()