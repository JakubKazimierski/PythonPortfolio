'''
Unit tests for CheckNums Method
October 2020 Jakub Kazimierski
'''

import unittest
import CheckNums

class test_CheckNums(unittest.TestCase):
    '''
    class with unit tests methods
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        method check if first num is less than second one
        then assert return true output
        '''
        output = CheckNums.CheckNums(1,11)
        self.assertEqual(output, "true")

    def test_EqualNumbers(self):
        '''
        method check if nums are equal
        then assert return -1
        '''
        output = CheckNums.CheckNums(-2,-2)
        self.assertEqual(output, "-1")

    def test_FalseOutput(self):
        '''
        method check if first num is greater
        than second one, then assert return false
        '''
        output = CheckNums.CheckNums(32,-2)
        self.assertEqual(output, "false")
    #endregion


if __name__ == "__main__":
    '''
    main method of unittest class
    '''
    unittest.main()