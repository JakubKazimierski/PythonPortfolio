'''
Unittests for ReversePolishNotation.py
January 2021 Jakub Kazimierski
'''

import unittest
import ReversePolishNotation

class test_ReversePolishNotation(unittest.TestCase):    
    '''
    Class with unittests for ReversePolishNotation.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = ReversePolishNotation.ReversePolishNotation("1 2 + 3 *")
        self.assertEqual(output, 9)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()