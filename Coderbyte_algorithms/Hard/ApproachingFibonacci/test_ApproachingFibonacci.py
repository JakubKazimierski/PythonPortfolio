'''
Unittests for ApproachingFibonacci.py
January 2021 Jakub Kazimierski
'''

import unittest
import ApproachingFibonacci

class test_ApproachingFibonacci(unittest.TestCase):    
    '''
    Class with unittests for ApproachingFibonacci.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = ApproachingFibonacci.ApproachingFibonacci([15, 1, 3])
        self.assertEqual(output, 2)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()