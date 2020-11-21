'''
Class contains unittests for ABCheck.py
Jakub Kazimierski October 2020
'''

import unittest
import ABCheckRegex

class test_ABCheck(unittest.TestCase):    
    '''
    Class with unittests for ABCheck.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is true
        for input with a and b letters separated by 3 indexes.
        '''
        output = ABCheckRegex.ABCheck("wwwwacccbdd")
        self.assertEqual(output, "true")

    def test_FewA(self):
        '''
        Checks if a few of letters a does not
        change expected true output.
        '''
        output = ABCheckRegex.ABCheck("aaacccbdd")
        self.assertEqual(output, "true")

    def test_FewAandB(self):
        '''
        Checks if a few of letters a and b does not
        change expected true output.
        '''
        output = ABCheckRegex.ABCheck("aaaccbbdd")
        self.assertEqual(output, "true")

    def test_FalseOutput(self):
        '''
        Checks if returned output is false
        for input without a and b letters separated by 3 indexes.
        '''
        output = ABCheckRegex.ABCheck("acsss    /cbbdd")
        self.assertEqual(output, "false")

    def test_VaroiusChars(self):
        '''
        Checks if returned output is true
        for input having a and b letters separated by 3 indexes
        and also containings non alphanumeric signs.
        '''
        output = ABCheckRegex.ABCheck("a/>0bd")
        self.assertEqual(output, "true")
        
    def test_CorectInputType(self):
        '''
        Checks if returned output is -1
        for input which is not string.
        '''
        output = ABCheckRegex.ABCheck(12)
        self.assertEqual(output, -1)

    def test_CorectInputLength(self):
        '''
        Checks if returned output is -1
        for input which is empty string.
        '''
        output = ABCheckRegex.ABCheck("")
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()