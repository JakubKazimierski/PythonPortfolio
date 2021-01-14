'''
Unittests for NumberEncoding.py
December 2020 Jakub Kazimierski
'''

import unittest
import NumberEncoding

class test_NumberEncoding(unittest.TestCase):    
    '''
    Class with unittests for NumberEncoding.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = NumberEncoding.NumberEncoding("Af5c a#!")
        self.assertEqual(output, "1653 1#!")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()