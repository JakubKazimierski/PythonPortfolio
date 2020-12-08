'''
Unittests for SnakeCase.py
December 2020 Jakub Kazimierski
'''

import unittest
import SnakeCase

class test_SnakeCase(unittest.TestCase):    
    '''
    Class with unittests for SnakeCase.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = SnakeCase.SnakeCase("BOB loves-coding")
        self.assertEqual(output, "bob_loves_coding")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''        
        output = SnakeCase.SnakeCase(6)
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()