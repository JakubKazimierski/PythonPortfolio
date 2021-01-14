'''
Unittestst for Primes.py
December 2020 Jakub Kazimierski
'''

import unittest
import Primes

class test_Primes(unittest.TestCase):    
    '''
    Class with unittests for Primes.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = Primes.Primes(19)
        self.assertEqual(output, "true")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()