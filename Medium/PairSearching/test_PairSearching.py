'''
Unittests fro PairSearching.py
December 2020 Jakub Kazimierski
'''

import unittest
import PairSearching

class test_PairSearching(unittest.TestCase):    
    '''
    Class with unittests for PairSearching.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = PairSearching.PairSearching(46)
        self.assertEqual(output, 2)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()