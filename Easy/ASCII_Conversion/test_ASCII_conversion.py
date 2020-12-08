'''
Unittests for ASCII_conversion.py
December 2020 Jakub Kazimierski
'''

import unittest
import ASCII_conversion

class test_ASCII_conversion(unittest.TestCase):    
    '''
    Class with unittests for ASCII_conversion.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = ASCII_conversion.ASCII_conversion("hello world")
        self.assertEqual(output, "104101108108111 119111114108100")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''        
        output = ASCII_conversion.ASCII_conversion(6)
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()