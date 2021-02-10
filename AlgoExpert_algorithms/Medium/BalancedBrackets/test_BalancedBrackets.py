'''
Unittests for BalancedBrackets.py
February 2021 Jakub Kazimierski
'''

import unittest
from BalancedBrackets import balancedBrackets

class test_BalancedBrackets(unittest.TestCase):    
    '''
    Class with unittests for BalancedBrackets.py
    '''

    def SetUp(self):
        '''
        Set Up input matrix.
        '''
        
        self.input = "([])(){}(())()()"
        self.output = True

        return self.input, self.output

    # region Unittests
    def test_Iterative_method(self):   
        '''
        Checks if output is correct.
        '''
        
        input_val, output_val = self.SetUp()
        
        method_output = balancedBrackets(input_val)
        self.assertEqual(method_output, output_val)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()