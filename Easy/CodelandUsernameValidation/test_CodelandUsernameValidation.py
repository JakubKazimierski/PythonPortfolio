'''
Unittests for CodelandUsernameValidation.py
October 2020 Jakub Kazimierski
'''

import unittest
import CodelandUsernameValidation

class test_CodelandUsernameValidation(unittest.TestCase):
    '''
    Class contains unittests for CodelandUsernameValidation.
    '''

    #region Unittests
    def test_AlbhapetClosure(self):
        '''
        Checks if name with other characters than defined in task
        will give output false.
        '''
        output = CodelandUsernameValidation.CodelandUsernameValidation("ass_ddd?")
        self.assertEqual(output, "false")


    def test_UsernameLengthTooShort(self):
        '''
        Checks if for username which is less than 4 characters
        output is false.
        '''
        output  = CodelandUsernameValidation.CodelandUsernameValidation("Abc")
        self.assertEqual(output, "false")   


    def test_UsernameLengthProper(self):
        '''
        Checks if for proper username which length is in range [4,25]
        output is true.
        '''
        output = CodelandUsernameValidation.CodelandUsernameValidation("Abc_cba")
        self.assertEqual(output, "true")   

    def test_UsernameLengthTooLong(self):
        '''
        Checks if for username which length is greater than 25
        output is false.
        '''
        output = CodelandUsernameValidation.CodelandUsernameValidation("Abcdefg_hijklmnoprsqtuwxyz12344")
        self.assertEqual(output, "false")   


    def test_UsernameFirstSign(self):
        '''
        Checks if output is false if username does not start with letter.
        '''
        output = CodelandUsernameValidation.CodelandUsernameValidation("_sAbc")
        self.assertEqual(output, "false")

    def test_UsernameLastSign(self):
        '''
        Checks if output is false when name ends with underscore.
        ''' 
        output = CodelandUsernameValidation.CodelandUsernameValidation("sAbc_")
        self.assertEqual(output, "false")
    #endregion
    

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()


