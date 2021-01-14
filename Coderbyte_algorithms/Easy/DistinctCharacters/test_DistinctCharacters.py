'''
Unittests for DistinctCharacters.py
December 2020 Jakub Kazimierski
'''

import unittest
import DistinctCharacters

class test_DistinctCharacters(unittest.TestCase):    
    '''
    Class with unittests for DistinctCharacters.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = DistinctCharacters.DistinctCharacters("abc123kkmmmm?")
        self.assertEqual(output, "false")

    
    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''        
        output = DistinctCharacters.DistinctCharacters(6)
        self.assertEqual(output, -1)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()