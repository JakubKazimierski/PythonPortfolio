'''
Unittestst for MatchingCharacters.py
December 2020 Jakub Kazimierski
'''

import unittest
import MatchingCharacters

class test_MatchingCharacters(unittest.TestCase):    
    '''
    Class with unittests for MatchingCharacters.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = MatchingCharacters.MatchingCharacters("ghececgkaem")
        self.assertEqual(output, 5)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()