'''
Unittests for QueenCheck.py
January 2021 Jakub Kazimierski
'''

import unittest
import QueenCheck

class test_QueenCheck(unittest.TestCase):    
    '''
    Class with unittests for QueenCheck.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        pass
        input_val =  ["(8,2)","(7,3)"]
        output = QueenCheck.QueenCheck(input_val)
        self.assertEqual(output, 3)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()