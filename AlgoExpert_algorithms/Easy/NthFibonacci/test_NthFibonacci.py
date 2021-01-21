'''
Unittests for NthFibonacci.py
January 2021 Jakub Kazimierski
'''

import unittest
import NthFibonacci

class test_NthFibonacci(unittest.TestCase):    
    '''
    Class with unittests for NthFibonacci.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = NthFibonacci.nthFibonacci(6)
        self.assertEqual(output, 5)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()