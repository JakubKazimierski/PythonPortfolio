'''
Unittests class for DashInsert.py
November 2020 Jakub Kazimierski
'''

import unittest
import DashInsert


class test_DashInserr(unittest.TestCase):
    '''
    Class contains unittests for DashInsert.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is equal to expected one.
        '''
        output = DashInsert.DashInsert("99946")
        self.assertEqual(output, "9-9-946")
    
    def test_OneSeparator(self):
        '''
        Checks if alghoritm works
        properly for just two odd nums coming after each other.
        '''
        output = DashInsert.DashInsert("56730")
        self.assertEqual(output, "567-30")
    
    def test_NoOddNums(self):
        '''
        Checks if output is correct
        if input has no odd numbers.
        '''
        output = DashInsert.DashInsert("246")
        self.assertEqual(output,"246")

    def test_TwoOddNums(self):
        '''
        Checks if algorithm works correct
        if input has just two values.
        '''
        output = DashInsert.DashInsert("79")
        self.assertEqual(output,"7-9")

    def test_IndexError(self):
        '''
        Checks if length is not proper assertion
        catches it and returns proper output error
        '''
        output = DashInsert.DashInsert("")
        self.assertEqual(output,-1)

    def test_TypeError(self):
        '''
        Checks if type is not correct assertion 
        catches it and return proper output error
        '''
        output = DashInsert.DashInsert(1)
        self.assertEqual(output,-1)

    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()    
