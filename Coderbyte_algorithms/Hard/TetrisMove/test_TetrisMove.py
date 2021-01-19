'''
Unittests for TetrisMove.py
January 2021 Jakub Kazimierski
'''

import unittest
import TetrisMove

class test_TetrisMove(unittest.TestCase):    
    '''
    Class with unittests for TetrisMove.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["T","4","3","2","3","5","2","0","1","2","4","3","4"]
        output = TetrisMove.TetrisMove(input_val)
        self.assertEqual(output, 2)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()