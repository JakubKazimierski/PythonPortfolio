'''
Unittests for MatrixPath.py
December 2020 Jakub Kazimierski
'''

import unittest
import MatrixPath

class test_MatrixPath(unittest.TestCase):    
    '''
    Class with unittests for MatrixPath.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = MatrixPath.MatrixPath(["11100", "10011", "10101", "10011"])
        self.assertEqual(output, 2)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()