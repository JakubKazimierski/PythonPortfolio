'''
Unittests for PascalsTriangle.py
January 2021 Jakub Kazimierski
'''

import unittest
import PascalsTriangle

class test_PascalsTriangle(unittest.TestCase):    
    '''
    Class with unittests for PascalsTriangle.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = PascalsTriangle.PascalsTriangle([1, 3, 3, 1])
        self.assertEqual(output, -1)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()