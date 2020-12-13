'''
Unittests for StringChanges.py
December 2020 Jakub Kazimierski
'''

import unittest
import StringChanges

class test_StringChanges(unittest.TestCase):    
    '''
    Class with unittests for StringChanges.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = StringChanges.StringChanges("abcNdgM")
        self.assertEqual(output, "abcgg")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = StringChanges.StringChanges(12)
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()