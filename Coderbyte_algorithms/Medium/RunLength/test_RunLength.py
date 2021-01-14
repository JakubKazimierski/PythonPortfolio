'''
Unittests for RunLength.py
December 2020 Jakub Kazimierski
'''

import unittest
import RunLength

class test_RunLength(unittest.TestCase):    
    '''
    Class with unittests for RunLength.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = RunLength.RunLength("wwwggop")
        self.assertEqual(output, "3w2g1o1p")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = RunLength.RunLength(11)
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()