'''
Unittests for Non_ConstructibleChange.py
February 2021 Jakub Kazimierski
'''

import unittest
from Non_ConstructibleChange import nonConstructibleChange

class test_Non_ConstructibleChange(unittest.TestCase):    
    '''
    Class with unittests for Non_ConstructibleChange.py
    '''

    def setUp(self):
        '''
        Sets up input and output.
        '''
        self.coins = [5, 7, 1, 1, 2, 3, 22]
        self.output = 20

        return self.coins, self.output
    
    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        coins, output = self.setUp()
        method_output = nonConstructibleChange(coins)
        self.assertEqual(output, method_output)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()