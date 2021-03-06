'''
Unittests for NumbersInPi.py
March 2021 Jakub Kazimierski
'''

import unittest
from NumbersInPi import numbersInPi

class test_NumbersInPi(unittest.TestCase):    
    '''
    Class with unittests for NumbersInPi.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''

        self.input_pi = "3141592653589793238462643383279"
        self.numbers =  ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]
        self.output = 2

        return self.input_pi, self.numbers, self.output

    # region Unittests
    def test_user_input(self):
        '''
        Checks if method works properly.
        '''
        pi, numbers, output = self.setUp()
        output_method = numbersInPi(pi, numbers)

        self.assertEqual(output, output_method)


   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()