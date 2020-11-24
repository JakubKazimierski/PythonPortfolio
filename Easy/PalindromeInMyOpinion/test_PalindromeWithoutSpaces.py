'''
Unittests for palindromeWithoutSpaces.py
October 2020 Jakub Kazimierski
'''
import unittest
import PalindromeWithoutSpaces


class test_PalindromeWithoutSpaces(unittest.TestCase):
    '''
    class with unittests for PalindromeWithoutSpaces.py
    '''

    #region Unittests
    def test_CorrectPalindrome(self):
        '''
        check if output is true for string which is palindrome
        '''
        output = PalindromeWithoutSpaces.Palindrome("assssa")
        self.assertEqual(output, "true")

    #personally i dont think "assss a" is palindorme, cause backward space is still kind of sign
    def test_PalindromeButSpaceIsAsciiCharAndNotAtTwinIndexes(self):
        '''
        check if output is false for string which is palindrome if we consider
        only letters but not spaces (but in this case space is count as a sign)
        '''
        output = PalindromeWithoutSpaces.Palindrome("assss a")
        self.assertEqual(output, "false")

    def test_CorrectSpacePalindrome(self):
        '''
        check if output is true for spaces
        whch are symetric in string
        '''
        output = PalindromeWithoutSpaces.Palindrome("a ssss a")
        self.assertEqual(output, "true")
    
    def test_EmptyInput(self):
        '''
        check if output is -1 for empty input
        '''
        output = PalindromeWithoutSpaces.Palindrome("")
        self.assertEqual(output, -1)
        
    def test_WrongInput(self):
        '''
        check if output is -1 for wrong type of input
        '''
        output = PalindromeWithoutSpaces.Palindrome(22)
        self.assertEqual(output, -1)
    #endregion

if __name__ == "__main__":
    '''
    main method for unittests class
    '''
    unittest.main()        