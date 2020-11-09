'''
Unittests for ExOh.py
October 2020 Jakub Kazimierski
'''

import unittest
import ExOh

class test_ExOh(unittest.TestCase):
    '''
    class with unittests for ExOh from codersbyte
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        check if output is true
        for equall numbers of x and o
        '''
        output = ExOh.ExOh("oxoxox")
        self.assertEqual(output, "true")

    def test_UpperAndLowerCase(self):
        '''
        check if Upper case change output
        '''
        output = ExOh.ExOh("oXOxOx")
        self.assertEqual(output, "true")

    def test_NotEqual(self):
        '''
        check if putput is false
        for not equal amount of x and o
        '''
        output = ExOh.ExOh("xxxo")
        self.assertEqual(output, "false")


    def test_SpaceInside(self):
        '''
        check if spaces
        change output
        '''
        output = ExOh.ExOh("oXO xOx")
        self.assertEqual(output, -1)

    def test_OtherSignsInside(self):
        '''
        check if other chars than letters
        change output
        '''
        output = ExOh.ExOh("oXO?><xOx")
        self.assertEqual(output, -1)

    def test_EmptyString(self):
        '''
        check output for empty string at input
        '''
        output = ExOh.ExOh("")
        self.assertEqual(output, -1)
    #endregion
    
if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()
        