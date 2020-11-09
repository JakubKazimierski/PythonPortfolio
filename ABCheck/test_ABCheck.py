'''
test cases for ABCheck from coderbyte

Jakub Kazimierski October 2020
'''


import unittest
import ABCheck

class test_ABCheck(unittest.TestCase):
    
    '''
    class of unittests
    created to test specified
    problems of ABCheck method
    '''

    #region Unittests
    def test_ProperOutput(self):
        
        '''
        check
        expected output
        which is true
        '''
        output = ABCheck.ABCheck("wwwwacccbdd")
        self.assertEqual(output, "true")


    def test_FewA(self):
        '''
        check if many of characters of a
        change proper output
        '''
        output = ABCheck.ABCheck("aaacccbdd")
        self.assertEqual(output, "true")

    def test_FewAandB(self):
        '''
        check if many characters of a and b
        change proper output
        '''

        output = ABCheck.ABCheck("aaaccbbdd")
        self.assertEqual(output, "true")

    def test_FalseOutput(self):
        '''
        check if false output is correcty found
        '''
        output = ABCheck.ABCheck("acsss    /cbbdd")
        self.assertEqual(output, "false")

    def test_VaroiusChars(self):
        '''
        check if other signs than letters
        work properly
        for output which should be true
        '''
        
        output = ABCheck.ABCheck("a/>0bd")
        self.assertEqual(output, "true")
        
    #endregion

if __name__ == "__main__":
    '''
    main method for test cases
    '''
    
    unittest.main()