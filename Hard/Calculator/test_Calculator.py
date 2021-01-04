'''
Unittests for Calculator.py
January 2021 Jakub Kazimierski
'''

import unittest
import Calculator

class test_Calculator(unittest.TestCase):    
    '''
    Class with unittests for Calculator.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = Calculator.Calculator("7-4-1+8(3)/2")
        self.assertEqual(output, 14)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()