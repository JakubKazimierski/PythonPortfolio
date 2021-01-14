'''
Unittests for OffLineMinimum.py
November 2020 Jakub Kazimierski
'''

import unittest
import OffLineMinimum

class test_OffLineMinimum(unittest.TestCase):
    '''
    Class contains unittests for OffLineMinimum.py
    '''

    #region Unittests

    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = OffLineMinimum.OffLineMinimum(["5","4","4","6","E","1","7","E","E","3","2"])
        self.assertEqual(output, "4,1,4")
    
    def test_E_atFirstIndex(self):
        '''
        Checks if for E at first index
        function does not return error.
        '''
        output = OffLineMinimum.OffLineMinimum(["E","5","4","6","E","1","7","E","E","3","2"])
        self.assertEqual(output, "4,1,5")
    
    def test_EmptyInput(self):
        '''
        Checks if for Empty input
        function returns ""
        '''
        output = OffLineMinimum.OffLineMinimum([])
        self.assertEqual(output, "")

    def test_WrongInputType(self):
        '''
        Checks if for wrong type of input
        function returns -1
        '''
        output = OffLineMinimum.OffLineMinimum(["E","2","3", 4,"E"])
        self.assertEqual(output, -1)


    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()