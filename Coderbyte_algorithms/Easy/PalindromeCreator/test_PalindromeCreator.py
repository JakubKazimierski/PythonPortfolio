'''
Unittests for PalindromeCreator.py
December 2020 Jakub Kazimierski
'''

import unittest
import PalindromeCreator

class test_PalindromeCreator(unittest.TestCase):
    '''
    Class contains unittests for
    PalindromeCreator.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = PalindromeCreator.PalindromeCreator("abjchba")
        self.assertEqual(output, "jc")

    def test_A(self):
        '''
        Checks if output is as expected if lack of one letter is enough to create palindrome.
        '''
        output = PalindromeCreator.PalindromeCreator("jjjhjjjk")
        self.assertEqual(output, "k")

    def test_NotPossible(self):
        '''
        Checks if output is equal "not possible.
        '''
        output = PalindromeCreator.PalindromeCreator("abcd")
        self.assertEqual(output, "not possible")


    def test_AlreadyPalindrome(self):
        '''
        Checks if output is equal to input.
        '''
        output = PalindromeCreator.PalindromeCreator("aba")
        self.assertEqual(output, "palindrome")

    def test_Short(self):
        '''
        Checks if output is equal to input.
        '''
        output = PalindromeCreator.PalindromeCreator("mmop")
        self.assertEqual(output, "op")


    def test_WrongInput(self):
        '''
        Checks if output is equal -1 if input is wrong.
        '''
        pass
        output = PalindromeCreator.PalindromeCreator(11)
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()