'''
Unittests for AlphabetSearching.py
December 2020 Jakub Kazimierski
'''

import unittest
import AlphabetSearching

class test_AlphabetSearching(unittest.TestCase):
    '''
    Class contains unittests for
    AlphabetSearching.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = AlphabetSearching.AlphabetSearching("zacxyjbbkfgtbhdaielqrm45pnsowtuv" )
        self.assertEqual(output, "true")

    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = AlphabetSearching.AlphabetSearching(12)
        self.assertEqual(output, -1)


    #endregion

if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()