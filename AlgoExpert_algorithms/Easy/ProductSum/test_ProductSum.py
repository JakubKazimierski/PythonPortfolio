'''
Unittests for ProductSum.py
January 2021 Jakub Kazimierski
'''

import unittest
import ProductSum

class test_ProductSum(unittest.TestCase):    
    '''
    Class with unittests for ProductSum.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr  = [[[[[5]]]]]
        output = ProductSum.productSum(input_arr)
        self.assertEqual(output, 600)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()