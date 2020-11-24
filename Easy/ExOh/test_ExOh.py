'''
Unittests for ExOh.py
October 2020 Jakub Kazimierski
'''

import unittest
import ExOh

class test_ExOh(unittest.TestCase):
    '''
    Class contains unittests for ExOh.py
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        Checks if output is true
        for equall numbers of x and o.
        '''
        output = ExOh.ExOh("oxoxox")
        self.assertEqual(output, "true")

    def test_UpperAndLowerCase(self):
        '''
        Checks if for uppercase letters
        algorithm works the same way as for lowercase.
        '''
        output = ExOh.ExOh("oXOxOx")
        self.assertEqual(output, "true")

    def test_NotEqual(self):
        '''
        Checks if output is false
        for not equal amount of x and o letters.
        '''
        output = ExOh.ExOh("xxxo")
        self.assertEqual(output, "false")


    def test_SpaceInside(self):
        '''
        Checks if forbdden sign appears in
        input, output is -1.
        '''
        output = ExOh.ExOh("oXO xOx")
        self.assertEqual(output, -1)

    def test_OtherSignsInside(self):
        '''
        Checks if forbdden sign appears in
        input, output is -1.
        '''
        output = ExOh.ExOh("oXO?><xOx")
        self.assertEqual(output, -1)

    def test_EmptyString(self):
        '''
        Checks if for empty input, assertion catches it
        and output is -1.
        '''
        output = ExOh.ExOh("")
        self.assertEqual(output, -1)
    #endregion
    
if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()
        