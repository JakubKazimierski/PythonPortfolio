'''
Unittests for PalindromeSwapper.py
December 2020 Jakub Kazimierski
'''

import unittest
import PalindromeSwapper

class test_PalindromeSwapper(unittest.TestCase):
    '''
    Class contains unittests for PalindromeSwapper.py
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = PalindromeSwapper.PalindromeSwapper("rcaecar")
        self.assertEqual(output, "racecar")

    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = PalindromeSwapper.PalindromeSwapper(12)
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittests.
    '''
    unittest.main()
