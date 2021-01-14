'''
Unittests for KnightJumps.py
January 2021 Jakub Kazimierski
'''

import unittest
import KnightJumps

class test_KnightJumps(unittest.TestCase):    
    '''
    Class with unittests for KnightJumps.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = KnightJumps.KnightJumps("(4 5)")
        self.assertEqual(output, 8)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()