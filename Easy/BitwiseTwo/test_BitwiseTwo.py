'''
Unittests for BitwiseTwo.py
December 2020 Jakub Kazimierski
'''

import unittest
import BitwiseTwo

class test_BitwiseTwo(unittest.TestCase):
    '''
    Class contains unittests for
    BitwiseTwo.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks is output is as expected.
        '''
        output = BitwiseTwo.BitwiseTwo(["10111", "01101"])
        self.assertEqual(output, "00101")

    def test_WrongInput(self):
        '''
        Checks is output is equal -1 if input is wrong.
        '''
        output = BitwiseTwo.BitwiseTwo([10111, "01101"])
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()