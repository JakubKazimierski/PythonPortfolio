'''
unittests for CodelandUsernameValidation method
October 2020 Jakub Kazimierski
'''

import unittest
import CodelandUsernameValidation

class test_CodelandUsernameValidation(unittest.TestCase):
    '''
    class with unittests for CodelandUsernameValidation
    '''

    #region Unittests
    def test_AlbhapetClosure(self):
        '''
        check if name with other characters than defined in task
        will give output false
        '''
        otherSigns_result = CodelandUsernameValidation.CodelandUsernameValidation("?><|\\")
        self.assertEqual(otherSigns_result, False)


    def test_UsernameLength(self):
        '''
        check if names length change output like defined in task true output is for 4-25 characters
        '''
        proper_result = CodelandUsernameValidation.CodelandUsernameValidation("Abc_deF")
        self.assertEqual(proper_result, True)   

        short_result  = CodelandUsernameValidation.CodelandUsernameValidation("Abc")
        self.assertEqual(short_result, False)   

        long_result  = CodelandUsernameValidation.CodelandUsernameValidation("AbcdefghijklmnoprstuwxyzABCDEFGH")
        self.assertEqual(long_result, False)   
    
    def test_UsernameFirstSign(self):
        '''
        check if output is true when name starts with letter, and uf is false when starts with
        other available sign
        '''
        with_firstLetter_result  = CodelandUsernameValidation.CodelandUsernameValidation("Abd_dc")
        self.assertEqual(with_firstLetter_result, True)

        without_firstLetter_result  = CodelandUsernameValidation.CodelandUsernameValidation("_sAbc")
        self.assertEqual(without_firstLetter_result, False)

    def test_UsernameLastSign(self):
        '''
        check if output is false when name ends with underscoere
        and if it is true when ends with letter
        '''
        with_lastLetter_result  = CodelandUsernameValidation.CodelandUsernameValidation("sAbcaa")
        self.assertEqual(with_lastLetter_result, True)
 
        without_lastLetter_result  = CodelandUsernameValidation.CodelandUsernameValidation("sAbc_")
        self.assertEqual(without_lastLetter_result, False)
    #endregion
    

if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()


