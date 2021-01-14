'''
Unittests for CamelCase.py
December 2020 Jakub Kazimierski
'''

import unittest
import CamelCase

class test_CamelCase(unittest.TestCase):    
    '''
    Class with unittests for CamelCase.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = CamelCase.CamelCase("BOB loves-coding")
        self.assertEqual(output, "bobLovesCoding")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''        
        output = CamelCase.CamelCase(6)
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()