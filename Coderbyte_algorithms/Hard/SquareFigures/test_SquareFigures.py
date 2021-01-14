'''
Unittests for SquareFigures.py
January 2021 Jakub Kazimierski
'''

import unittest
import SquareFigures

class test_SquareFigures(unittest.TestCase):    
    '''
    Class with unittests for SquareFigures.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = SquareFigures.SquareFigures(6)
        self.assertEqual(output, 317)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()