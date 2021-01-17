'''
Unittests for MaximalSquare.py
January 2021 Jakub Kazimierski
'''

import unittest
import MaximalSquare

class test_MaximalSquare(unittest.TestCase):    
    '''
    Class with unittests for MaximalSquare.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val =  ["0111", "1111", "1111", "1111"]
        output = MaximalSquare.MaximalSquare(input_val)
        self.assertEqual(output, 9)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()