'''
Unittests for MatrixBorder.py
January 2021 Jakub Kazimierski
'''

import unittest
import MatrixBorder

class test_MatrixBorder(unittest.TestCase):    
    '''
    Class with unittests for MatrixBorder.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = MatrixBorder.MatrixBorder( ["(0,1,0,1)","(1,1,1,1)","(0,1,0,1)","(1,1,1,1)"])
        self.assertEqual(output, 2)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()