'''
Unittests for CaesarCipherEncryptor.py
January 2021 Jakub Kazimierski
'''

import unittest
import CaesarCipherEncryptor

class test_CaesarCipherEncryptor(unittest.TestCase):    
    '''
    Class with unittests for CaesarCipherEncryptor.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        pass
        input_str  = "xyz"
        input_key = 2
        output = CaesarCipherEncryptor.caesarCipherEncryptor(input_str, input_key)
        self.assertEqual(output, "zab")
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()