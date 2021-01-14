'''
Unittests for FibonacciChecker.py
December 2020 Jakub Kazimierski
'''

import unittest
import FibonacciChecker

class test_FibonacciChecker(unittest.TestCase):    
    '''
    Class with unittests for FibonacciChecker.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = FibonacciChecker.FibonacciChecker(34)
        self.assertEqual(output, "yes")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()