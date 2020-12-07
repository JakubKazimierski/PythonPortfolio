'''
Unittests for LargestFour.py
December 2020 Jakub Kazimierski
'''

import unittest
import LargestFour

class test_LargestFour(unittest.TestCase):    
    '''
    Class with unittests for LargestFour.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = LargestFour.LargestFour([4, 5, -2, 3, 1, 2, 6, 6])
        self.assertEqual(output, 21)

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = LargestFour.LargestFour("6")
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()