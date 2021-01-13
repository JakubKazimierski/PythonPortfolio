'''
Unittests for NimWinner.py
January 2021 Jakub Kazimierski
'''

import unittest
import  NimWinner

class test_NimWinner(unittest.TestCase):    
    '''
    Class with unittests for NimWinner.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = NimWinner.NimWinner([1, 2, 3])
        self.assertEqual(output, 2)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()