'''
Unittests for PalindromeTwo.py
December 2020 Jakub Kazimierski
'''

import unittest
import PalindromeTwo

class test_PalindromeTwo(unittest.TestCase):    
    '''
    Class with unittests for PalindromeTwo.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = PalindromeTwo.PalindromeTwo("Anne, I vote more cars race Rome-to-Vienna" )
        self.assertEqual(output, "true")

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()