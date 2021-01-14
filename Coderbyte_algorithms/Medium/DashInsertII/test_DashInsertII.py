'''
Unittests for DashInsertII.py
December 2020 Jakub Kazimierski
'''

import unittest
import DashInsertII

class test_DashInsertII(unittest.TestCase):    
    '''
    Class with unittests for DashInsertII.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = DashInsertII.DashInsertII(4546793)
        self.assertEqual(output, "454*67-9-3")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()