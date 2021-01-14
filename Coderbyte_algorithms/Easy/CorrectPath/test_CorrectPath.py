'''
Unittests for CorrectPath.py
December 2020 Jakub Kazimierski
'''

import unittest
import CorrectPath

class test_CorrectPath(unittest.TestCase):
    '''
    Class contains unittests for
    CorrectPath.py
    '''

    #region Unittests 
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = CorrectPath.CorrectPath("r?d?drdd" )
        self.assertEqual(output, "rrdrdrdd")

    def test_ExpectedOutputNextExample(self):
        '''
        Checks if output is as expected.
        '''
        output = CorrectPath.CorrectPath("???rrurdr?")
        self.assertEqual(output, "dddrrurdrd")

    def test_WrongInput(self):
        '''
        Checks if output is equal -1 if input is wrong.
        '''
        output = CorrectPath.CorrectPath("2")
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()