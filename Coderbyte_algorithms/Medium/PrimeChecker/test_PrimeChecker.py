'''
Unittests for PrimeChecker.py
December 2020 Jakub Kazimierski
'''

import unittest
import PrimeChecker

class test_PrimeChecker(unittest.TestCase):    
    '''
    Class with unittests for PrimeChecker.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = PrimeChecker.PrimeChecker(910)
        self.assertEqual(output, 1)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()