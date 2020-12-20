'''
Unittests for SymmetricTree.py
December 2020 Jakub Kazimierski
'''

import unittest
import SymmetricTree

class test_SymmetricTree(unittest.TestCase):    
    '''
    Class with unittests for SymmetricTree.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = SymmetricTree.SymmetricTree(["1", "2", "2", "3", "#", "#", "3"] )
        self.assertEqual(output, "true")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()