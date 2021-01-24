'''
Unittests for MoveElementToEnd.py
January 2021 Jakub Kazimierski
'''

import unittest
import MoveElementToEnd

class test_MoveElementToEnd(unittest.TestCase):    
    '''
    Class with unittests for MoveElementToEnd.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_arr = [2, 1, 2, 2, 2, 3, 4, 2]
        toMove = 2
        output = MoveElementToEnd.moveElementToEnd(input_arr, toMove)
        self.assertEqual(output, [1, 3, 4, 2, 2, 2, 2, 2] )
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()