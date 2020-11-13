'''
Unittests class for DashInsert.py
November 2020 Jakub Kazimierski
'''

import unittest
import DashInsert


class test_DashInserr(unittest.TestCase):
    '''
    class contains unittests for DashInsert.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        check if alghoritm works properly
        for few odd numbers
        '''
        output = DashInsert.DashInsert("99946")
        self.assertEqual(output, "9-9-946")
    
    def test_OneSeparator(self):
        '''
        check if alghoritm works
        properly for just two odd nums coming after each other
        '''
        output = DashInsert.DashInsert("56730")
        self.assertEqual(output, "567-30")
    
    def test_NoOddNums(self):
        '''
        check if output is correct
        inf input has no odd numbers
        '''
        output = DashInsert.DashInsert("246")
        self.assertEqual(output,"246")

    def test_TwoOddNums(self):
        '''
        check if output is correct
        inf input has just two values
        '''
        output = DashInsert.DashInsert("79")
        self.assertEqual(output,"7-9")

    def test_IndexError(self):
        '''
        check if  length is not properly
        function catches it and return proper
        output error
        '''
        output = DashInsert.DashInsert("")
        self.assertEqual(output,-1)

    def test_TypeError(self):
        '''
        check if  type is not correct
        function catches it and return proper
        output error
        '''
        output = DashInsert.DashInsert(1)
        self.assertEqual(output,-1)


    #endregion

if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()    
