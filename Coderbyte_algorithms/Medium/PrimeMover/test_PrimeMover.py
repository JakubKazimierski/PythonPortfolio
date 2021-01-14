'''
Unittests for PrimeMover.py
December 2020 Jakub Kazimierski
'''

import unittest
import PrimeMover

class test_PrimeMover(unittest.TestCase):    
    '''
    Class with unittests for PrimeMover.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = PrimeMover.PrimeMover(16)
        self.assertEqual(output, 53)

    # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()