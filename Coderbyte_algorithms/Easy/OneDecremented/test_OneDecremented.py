'''
Unittests for OneDecremented.py
December 2020 Jakub Kazimierski
'''

import unittest
import OneDecremented

class test_OneDecremented(unittest.TestCase):    
    '''
    Class with unittests for OneDecremented.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = OneDecremented.OneDecremented("9876541110")
        self.assertEqual(output, 6)

    
    def test_OneDigit(self):
        '''
        Checks if returned output is equal 0 for one digit at input.
        '''
        output = OneDecremented.OneDecremented("9")
        self.assertEqual(output, 0)

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = OneDecremented.OneDecremented(12)
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()