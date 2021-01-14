'''
Unittests for ChessboardTraveling.py
January 2021 Jakub Kazimierski
'''

import unittest
import ChessboardTraveling

class test_ChessboardTraveling(unittest.TestCase):    
    '''
    Class with unittests for ChessboardTraveling.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = "(1 1)(3 3)"
        output = ChessboardTraveling.ChessboardTraveling(input_val)
        self.assertEqual(output, 6)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()