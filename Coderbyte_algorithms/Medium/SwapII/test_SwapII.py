'''
Unittests for SwapII.py
December 2020 Jakub Kazimierski
'''

import unittest
import SwapII

class test_SwapII(unittest.TestCase):    
    '''
    Class with unittests for SwapII.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = SwapII.SwapII("6Hello4 -8World, 7 yes3")
        self.assertEqual(output, "4hELLO6 -8wORLD, 7 YES3")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()