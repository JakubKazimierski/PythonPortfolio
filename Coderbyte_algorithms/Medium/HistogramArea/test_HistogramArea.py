'''
Unittestst for HistogramArea.py
December 2020 Jakub Kazimierski
'''

import unittest
import HistogramArea

class test_HistogramArea(unittest.TestCase):    
    '''
    Class with unittests for HistogramArea.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = HistogramArea.HistogramArea([1, 3, 2, 1, 2])
        self.assertEqual(output, 5)

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()