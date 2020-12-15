'''
Unittests for CaesarCipher.py
December 2020 Jakub Kazimierski
'''

import unittest
import CaesarCipher

class test_CaesarCipher(unittest.TestCase):    
    '''
    Class with unittests for CaesarCipher.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = CaesarCipher.CaesarCipher("Caesar, Cipher", 2)
        self.assertEqual(output, "Ecguct, Ekrjgt")

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()