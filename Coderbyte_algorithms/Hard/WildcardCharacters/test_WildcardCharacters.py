'''
Unittests for WildcardCharacters.py
January 2021 Jakub Kazimierski
'''

import unittest
import WildcardCharacters

class test_WildcardCharacters(unittest.TestCase):    
    '''
    Class with unittests for WildcardCharacters.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_val = "*{1}*{1} rt"
        output = WildcardCharacters.WildcardCharacters(input_val)
        self.assertEqual(output, "true")
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()