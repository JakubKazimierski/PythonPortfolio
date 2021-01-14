'''
Unittests for EightQueens.py
December 2020 Jakub Kazimierski
'''

import unittest
import EightQueens

class test_EightQueens(unittest.TestCase):    
    '''
    Class with unittests for EightQueens.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val =  ["(1,1)", "(7,2)", "(4,3)", "(6,4)", "(8,5)", "(2,6)", "(5,7)", "(5,8)"]
        output = EightQueens.EightQueens(input_val)
        self.assertEqual(output, "(8,5)")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()