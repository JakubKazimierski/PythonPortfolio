'''
Unittests for ProductDigits.py
December 2020 Jakub Kazimierski
'''
import unittest
import ProductDigits

class test_ProductDigits(unittest.TestCase):
    '''
    Class contains unittests for
    ProductDigits.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = ProductDigits.ProductDigits(24)
        self.assertEqual(output, 2)

    def test_PrimeInput(self):
        '''
        Checks if for prime number at input, output is proper warning.
        '''
        output = ProductDigits.ProductDigits(23)
        self.assertEqual(output, "This is prime number")


    def test_WrongInput(self):
        '''
        Checks if output is equal -1 if input is wrong.
        '''
        output = ProductDigits.ProductDigits("as")
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()