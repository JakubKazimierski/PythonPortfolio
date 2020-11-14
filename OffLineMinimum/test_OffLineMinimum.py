'''
Unittests for OffLineMinimum.py
November 2020 Jakub Kazimierski
'''

import unittest
import OffLineMinimum

class test_OffLineMinimum(unittest.TestCase):
    '''
    class contains unittests for
    OffLineMinimum.py
    '''

    #region Unittests

    def test_ExpectedOutput(self):
        '''
        check if for knowing output
        function returns it
        '''
        output = OffLineMinimum.OffLineMinimum(["5","4","6","E","1","7","E","E","3","2"])
        self.assertEqual(output, "4,1,5")
    
    def test_E_atFirstIndex(self):
        '''
        check if for E
        at first index
        function does not return error
        '''
        output = OffLineMinimum.OffLineMinimum(["E","5","4","6","E","1","7","E","E","3","2"])
        self.assertEqual(output, "4,1,5")
    
    def test_EmptyInput(self):
        '''
        check if for Empty input
        function returns -1
        '''
        output = OffLineMinimum.OffLineMinimum([])
        self.assertEqual(output, -1)

    def test_WrongInputType(self):
        '''
        check if for wrong type of input
        function returns -1
        '''
        output = OffLineMinimum.OffLineMinimum(["E","2","3", 4,"E"])
        self.assertEqual(output, -1)


    #endregion

if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()