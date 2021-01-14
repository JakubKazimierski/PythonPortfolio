'''
Unittests for PolynomialExpansion.py
January 2021 Jakub Kazimierski
'''

import unittest
import PolynomialExpansion

class test_PolynomialExpansion(unittest.TestCase):    
    '''
    Class with unittests for PolynomialExpansion.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''   
        output = PolynomialExpansion.PolynomialExpansion("(2x^2+4)(6x^3+3)")
        self.assertEqual(output, "12x^5+24x^3+6x^2+12")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()