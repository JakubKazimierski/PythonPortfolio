'''
Unittests for ArrayOfProducts.py
January 2021 Jakub Kazimierski
'''

import unittest
import ArrayOfProducts

class test_ArrayOfProducts(unittest.TestCase):    
    '''
    Class with unittests for ArrayOfProducts.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr  = [5, 1, 4, 2]
        output = ArrayOfProducts.arrayOfProducts(input_arr)
        self.assertEqual(output, [8, 40, 10, 20])
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()