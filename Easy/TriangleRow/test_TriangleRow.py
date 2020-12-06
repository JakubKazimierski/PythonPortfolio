'''
Unittests for TriangleRow.py
December 2020 Jakub Kazimierski
'''

import unittest
import TriangleRow

class test_TriangleRow(unittest.TestCase):
    '''
    Class contains unittests for TriangleRow.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is sorted in alphabetical order.
        '''
        pass
        output = TriangleRow.TriangleRow(5)
        self.assertEqual(output, 32)

    def test_WrongInput(self):
        '''
        Checks if output is -1 when input is wrong type.
        '''
        output = TriangleRow.TriangleRow("as")
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests' Class.
    '''
    unittest.main()