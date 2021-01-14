'''
Unittests for BoggleSolver.py
December 2020 Jakub Kazimierski
'''

import unittest
import BoggleSolver

class test_BoggleSolver(unittest.TestCase):    
    '''
    Class with unittests for BoggleSolver.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = BoggleSolver.BoggleSolver(["rbfg, ukop, fgub, mnry", "bog,bop,gup,fur,ruk"])
        self.assertEqual(output, "true")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()