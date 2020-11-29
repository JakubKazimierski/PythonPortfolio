'''
Unittests for OtherProducts.py
November 2020 Jakub Kazimierski
'''

import unittest
import OtherProducts

class test_OtherProducts(unittest.TestCase):
    '''
    Class contains unittests for OtherProducts.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Cheks if output is as expected.
        '''
        output = OtherProducts.OtherProducts([1,2,3,4,5])
        self.assertEqual(output, "120-60-40-30-24")

    def test_WrongInput(self):
        '''
        Cheks if output is equal -1 for worng input type.
        '''
        output = OtherProducts.OtherProducts(["1",2,3,4,5])
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()
