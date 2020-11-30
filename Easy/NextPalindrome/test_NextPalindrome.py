'''
Unittests for NextPalindrome.py
November 2020 Jakub Kazimierski
'''

import unittest
import NextPalindrome

class test_NextPalindrome(unittest.TestCase):
    '''
    Class contains unittests for NextPalindrome.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Cheks if output is as expected.
        '''
        output = NextPalindrome.NextPalindrome(2)
        self.assertEquals(output, 3)
               

    def test_WrongInput(self):
        '''
        Checks if for wrong input output is equal -1.
        '''
        output = NextPalindrome.NextPalindrome("5")
        self.assertEquals(output, -1)
        
    # endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()