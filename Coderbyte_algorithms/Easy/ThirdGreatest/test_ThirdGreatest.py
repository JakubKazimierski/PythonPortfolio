'''
Unittests for ThirdGreatest.py
November 2020 Jakub Kazimierski
'''

import unittest
import ThirdGreatest


class test_ThirdGreatest(unittest.TestCase):
    '''
    Class contains unittests for ThirdGreatest.py
    '''

    #region Unitests
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = ThirdGreatest.ThirdGreatest(["coder", "byte", "code"])
        self.assertEqual(output, "code")
    
    def test_SameLengthWords(self):
        '''
        Checks if alghoritm works properly with words having the same length.
        '''
        output = ThirdGreatest.ThirdGreatest(["aaaa", "bbbb", "cccc", "dddd"])
        self.assertEqual(output, "cccc")
    
    def test_WrongTypeInInput(self):
        '''
        Checks if method returns -1 when find wrong type.
        '''
        output = ThirdGreatest.ThirdGreatest(12)
        self.assertEqual(output, -1)

    #endregion



if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()    