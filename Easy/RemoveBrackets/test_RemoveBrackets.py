'''
Unittests for RemoveBrackets.py
December 2020 Jakub Kazimierski
'''

import unittest
import RemoveBrackets

class test_RemoveBrackets(unittest.TestCase):
    '''
    Class contains unittests for RemoveBrackets.py
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = RemoveBrackets.RemoveBrackets("(()))" )
        self.assertEqual(output, 1)

    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = RemoveBrackets.RemoveBrackets(12)
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittests.
    '''
    unittest.main()
