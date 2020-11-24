'''
Unittests for ThirdGreatestOriginall.py
November 2020 Jakub Kazimierski
'''

import unittest
import ThirdGreatestOriginall


class test_ThirdGreatest(unittest.TestCase):
    '''
    class contains unittests for ThirdGreatestOriginall.py
    '''

    #region Unitests
    def test_ExpectedOutput(self):
        '''
        check if output is as expected
        '''
        output = ThirdGreatestOriginall.ThirdGreatestOriginall(["coder", "byte", "code"])
        self.assertEqual(output, "code")
    
    def test_SameLengthWords(self):
        '''
        check if alghoritm works
        properly with words having same length
        '''
        output = ThirdGreatestOriginall.ThirdGreatestOriginall(["aaaa", "bbbb", "cccc", "dddd"])
        self.assertEqual(output, "cccc")

    def test_WrongSignsInInput(self):
        '''
        check if alghoritm returns -1
        when find wrong sign
        '''
        output = ThirdGreatestOriginall.ThirdGreatestOriginall(["aaaa", "b>bbb", "cccc", "dddd"])
        self.assertEqual(output, -1)
    #endregion

    def test_WrongTypeInInput(self):
        '''
        check if alghoritm returns -1
        when find wrong Type
        '''
        output = ThirdGreatestOriginall.ThirdGreatestOriginall(12)
        self.assertEqual(output, -1)
    #endregion



if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()    