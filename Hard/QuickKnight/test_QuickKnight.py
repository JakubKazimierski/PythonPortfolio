'''
Unittests for QuickKnight.py
January 2021 Jakub Kazimierski
'''

import unittest
import QuickKnight

class test_QuickKnight(unittest.TestCase):    
    '''
    Class with unittests for QuickKnight.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = QuickKnight.QuickKnight("(2 3)(7 5)")
        self.assertEqual(output, 3)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()