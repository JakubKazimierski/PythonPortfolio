'''
Unittests for VowelSquare.py
December 2020 Jakub Kazimierski
'''

import unittest
import VowelSquare

class test_VowelSquare(unittest.TestCase):
    '''
    Class contains unittests for VowelSquare.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is sorted in alphabetical order.
        '''
        output = VowelSquare.VowelSquare(["aqrst", "ukaei", "ffooo"])
        self.assertEqual(output, "1-2")

    def test_NotFound(self):
        '''
        Checks if output is equal "not found" if none of expected matrix exist.
        '''
        output = VowelSquare.VowelSquare(["uk", "ff"])
        self.assertEqual(output, "not found")

    def test_WrongInput(self):
        '''
        Checks if output is -1 when input is wrong type.
        '''
        output = VowelSquare.VowelSquare(12)
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests' Class.
    '''
    unittest.main()