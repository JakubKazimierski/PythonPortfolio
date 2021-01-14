'''
Unittests for AlphabetRunEncryption.py
January 2021 Jakub Kazimierski
'''

import unittest
import AlphabetRunEncryption

class test_AlphabetRunEncryption(unittest.TestCase):    
    '''
    Class with unittests for AlphabetRunEncryption.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = "cdefghijklmnnmlkjihgfedcb"
        output = AlphabetRunEncryption.AlphabetRunEncryption(input_val)
        self.assertEqual(output, "boa")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()