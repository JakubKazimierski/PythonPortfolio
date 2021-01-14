'''
Unittests for MatrixSpiral.py
December 2020 Jakub Kazimierski
'''

import unittest
import MatrixSpiral

class test_MatrixSpiral(unittest.TestCase):    
    '''
    Class with unittests for MatrixSpiral.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = ["[1, 2, 3]", "[4, 5, 6]", "[7, 8, 9]"]
        output = MatrixSpiral.MatrixSpiral(input_val)
        self.assertEqual(output, "1,2,3,6,9,8,7,4,5")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()