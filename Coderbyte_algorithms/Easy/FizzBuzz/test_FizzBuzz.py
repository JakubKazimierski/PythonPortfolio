'''
Unittests for FizzBuzz.py
December 2020 Jakub Kazimierski
'''

import unittest
import FizzBuzz

class test_FizzBuzz(unittest.TestCase):    
    '''
    Class with unittests for FizzBuzz.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = FizzBuzz.FizzBuzz(16)
        self.assertEqual(output, "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = FizzBuzz.FizzBuzz("12")
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()