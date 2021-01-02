'''
Unittests for SudokuQuadrantChecker.py
January 2021 Jakub Kazimierski
'''

import unittest
import SudokuQuadrantChecker

class test_SudokuQuadrantChecker(unittest.TestCase):    
    '''
    Class with unittests for SudokuQuadrantChecker.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["(1,2,3,4,5,6,7,8,1)","(x,x,x,x,x,x,x,x,x)",\
            "(x,x,x,x,x,x,x,x,x)","(1,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)",\
                "(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)",\
                    "(x,x,x,x,x,x,x,x,x)"]
        
        output = SudokuQuadrantChecker.SudokuQuadrantChecker(input_val)
        self.assertEqual(output, "1,3,4")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()