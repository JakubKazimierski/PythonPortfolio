'''
Unittests for TripleDouble.py
December 2020 Jakub Kazimierski
'''

import unittest
import TripleDouble

class test_TripleDouble(unittest.TestCase):    
    '''
    Class with unittests for TripleDouble.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = TripleDouble.TripleDouble(451999277, 41177722899)
        self.assertEqual(output, 1)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()